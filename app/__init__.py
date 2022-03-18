# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run

from flask import Flask, g, render_template, request, redirect, url_for
import cv2
import numpy as np
import sqlite3
import pickle
import random
import pandas as pd
import io
import base64
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
import keras
#from keras.models import load_model
from keras.preprocessing import image
from numpy import expand_dims
from tensorflow.keras.preprocessing.image import ImageDataGenerator

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('../static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Load the model

model = tf.keras.models.load_model("ed-model/InceptionV3_Ver2.h5")

def get_message_db():
    # Check whether there is a database called message_db in the g attribute of the app
    if 'message_db' not in g:
        #  If not, then connect to that database, ensuring that the connection is an attribute of g
        g.message_db = sqlite3.connect("messages_db.sqlite")

    if g.message_db is not None:
        cursor = g.message_db.cursor()
        # Check whether a table called messages exists in message_db, and create it if not
        sql_create_messages_table = """ CREATE TABLE IF NOT EXISTS messages (
                                    id integer,
                                    handle text,
                                    messages text
                                ); """
        cursor.execute(sql_create_messages_table)
    # Return the connection
    return g.message_db

def insert_message(request):
    # open the connection
    g.message_db = get_message_db()
    cursor = g.message_db.cursor()
    # Extract message and handle
    message = request.form["message"]
    message = message.replace("'", "''")
    handle = request.form["handle"]
    
    if handle == "":
        handle = "Anonymous"
    handle = handle.replace("'", "''")

    # get nrow and assign unique id
    n_row = cursor.execute('select * from messages;')
    nrow = len(n_row.fetchall()) + 1
    
    # add a new row to messages database
    cursor.execute("INSERT INTO messages (id, handle, messages) VALUES ({nrow}, '{handle}', '{message}')".format(
        nrow = nrow, handle = handle, message = message))
    # Save the change
    g.message_db.commit()
    # close the connection
    g.message_db.close()


def random_messages(n):
    # open the connection
    g.message_db = get_message_db()
    # Get a collection of n random messages from the message_db, or fewer if necessary
    messages = pd.read_sql_query("SELECT * FROM messages WHERE id IN (SELECT id FROM messages ORDER BY RANDOM() LIMIT {n})".format(n = n), g.message_db)
    # close the connection
    g.message_db.close()
    return messages

# Create main page (fancy)
@app.route('/')
def main():
    return render_template('main_better.html')

# File uploads and interfacing with complex Python
# nontrivial version: makes a prediction and shows a viz
@app.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        try:
            # retrieve the image
            img = request.files["image"]
            # filename = secure_filename("img")
            filename = "img.jpg"
            # save image to our local desktop
            img.save(os.path.join(app.root_path, "static/uploads", filename))
            return redirect('/result')
        except:
            return render_template('upload.html', error=True)

@app.route('/result/', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        filename = "img.jpg"
        img1 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # read the image
        img = cv2.imread(os.path.join(app.root_path, "static/uploads", "img.jpg"))
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  
        # Draw rectangle around the faces and crop the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            faces = img[y:y + h, x:x + w]
            # save the original image with rectangle
            cv2.imwrite(os.path.join(app.root_path, "static/uploads", "face.jpg"), faces)
            
        # detected image
        cv2.imwrite(os.path.join(app.root_path, "static/uploads", "detected.jpg"), img)

        # read the image
        face = os.path.join(app.config['UPLOAD_FOLDER'], "face.jpg")
        detected = os.path.join(app.config['UPLOAD_FOLDER'], "detected.jpg")

        img = image.load_img(os.path.join(app.root_path, "static/uploads", "face.jpg"), target_size=(144,144))
        data  = image.img_to_array(img)
        # convert to numpy array

        # expand dimension to one sample
        samples = expand_dims(data, 0)

        # create image data augmentation generator
        preprocess_fun = tf.keras.applications.inception_v3.preprocess_input
        datagen = ImageDataGenerator(rescale = 1./255,
                                        preprocessing_function=preprocess_fun)
        it = datagen.flow(samples, batch_size=1)

        CLASS_LABELS  = ['anger', 'disgust', 'fear', 'happy', 'neutral', 'sadness', "surprise"]
        index = np.argmax(model.predict(it), axis = 1)[0]
        label = CLASS_LABELS[index]

        return render_template('result.html', image = face, labels = label, image1 = detected)
    else:
        try:
            # if user's emotion is predicted as negative and a quote is requested
            if request.form['ans'] == "neg-quote":
                df1 = pd.read_csv("Quote_scraper/calm.csv")
                df2 = pd.read_csv("Quote_scraper/relax.csv")
                df = pd.concat([df1, df2])
                # randomly select a quote from a combined df
                getonequote = df.iloc[random.randint(0, df.shape[0])]
                writer = getonequote['author']
                text = getonequote['quote']
                return render_template('quote.html', writers = writer, texts = text)
            # if user's emotion is predicted as positive and a quote is requested
            elif request.form['ans'] == "pos-quote":
                df1 = pd.read_csv("Quote_scraper/fun.csv")
                df2 = pd.read_csv("Quote_scraper/happy.csv")
                df = pd.concat([df1, df2])
                # randomly select a quote from a combined df
                getonequote = df.iloc[random.randint(0, df.shape[0])]
                writer = getonequote['author']
                text = getonequote['quote']
                return render_template('quote.html', writers = writer, texts = text)
            # if a feedback is requested
            elif request.form['ans'] == "feedback":
                return redirect(url_for('feedback'))
            # if user's emotion is predicted as positive and a video is requested
            elif request.form['ans'] == "pos-video":
                df = pd.read_csv("Youtube_scraper/funny.csv")
                # randomly select a funny video
                getonequote = df.iloc[random.randint(0, df.shape[0])]
                link = getonequote['link']
                link = link.replace("https://www.youtube.com/watch?v=","https://www.youtube.com/embed/")
                title = getonequote['title']
                return render_template('video.html', link = link, title = title)
            # if user's emotion is predicted as negative and a video is requested
            elif request.form['ans'] == "neg-video":
                df = pd.read_csv("Youtube_scraper/relax.csv")
                # randomly select a relaxing video
                getonequote = df.iloc[random.randint(0, df.shape[0])]
                link = getonequote['link']
                link = link.replace("https://www.youtube.com/watch?v=","https://www.youtube.com/embed/")
                title = getonequote['title']
                return render_template('video.html', link = link, title = title)
            else:
                return render_template('thanks.html')
        except:
            return render_template('result.html', error=True)

@app.route('/feedback/', methods=['POST', 'GET'])
def feedback():
    if request.method == 'GET':
        return render_template('feedback.html')
    else: # if request.method == 'POST'
        try:
            insert_message(request)
            return render_template('feedback.html', thanks = True)
        except:
            return render_template('feedback.html', error = True)
            

@app.route('/feedbacksummary/')
def feedbacksummary():
    try:
        messages = random_messages(10)
        return render_template('feedbacksummary.html', messages = messages)
    except:
        return render_template('feedbacksummary.html', error = True)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response
