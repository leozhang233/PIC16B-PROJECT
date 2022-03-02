# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run

from flask import Flask, g, render_template, request, redirect, url_for
import sklearn as sk
import numpy as np
import pickle
import random
import pandas as pd
import io
import base64
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
import keras
# from keras.models import load_model
from keras.preprocessing import image
from numpy import expand_dims
from tensorflow.keras.preprocessing.image import ImageDataGenerator

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('../static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Load the model

model = tf.keras.models.load_model("ed-model/InceptionV3_Ver2.h5")

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
            # filename = secure_filename("img.png")
            filename = "img"
            # save image to our local desktop
            img.save(os.path.join(app.root_path, "static/uploads", filename))
            return redirect('/result')
        except:
            return render_template('upload.html', error=True)

@app.route('/result/', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        filename = "img"
        # read the image
        img = image.load_img(os.path.join(app.root_path, "static/uploads", filename), target_size=(144,144))

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

        return render_template('result.html', image = img, labels = "happy")
    else:
        try:
            if request.form['ans'] == "neg-quote":
                df1 = pd.read_csv("calm.csv")
                df2 = pd.read_csv("relax.csv")
                df = pd.concat([df1, df2])
                getonequote = df.iloc[random.randint(0, df.shape[0])]
                writer = getonequote['author']
                text = getonequote['quote']
                return render_template('quote.html', writers = writer, texts = text)
            elif request.form['ans'] == "pos-quote":
                df1 = pd.read_csv("fun.csv")
                df2 = pd.read_csv("happy.csv")
                df = pd.concat([df1, df2])
                getonequote = df.iloc[random.randint(0, df.shape[0])]
                writer = getonequote['author']
                text = getonequote['quote']
                return render_template('quote.html', writers = writer, texts = text)
            elif request.form['ans'] == "feedback":
                return render_template('feedback.html')
        except:
            return render_template('result.html', error=True)


