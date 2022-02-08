# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request
import sklearn as sk
import numpy as np
import pickle
import random

import io
import base64
from werkzeug.utils import secure_filename
import os
# from werkzeug.utils import secure_filename
# Create web app, run with flask run
# (set "FLASK_ENV" variable to "development" first!!!)

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('../static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create main page (fancy)

@app.route('/')
def main():
    return render_template('main_better.html')

# File uploads and interfacing with complex Python
# nontrivial version: makes a prediction and shows a viz
@app.route('/submit-advanced/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            # retrieve the image
            img = request.files["image"]
            filename = secure_filename(img.filename)
            # save image to our local desktop
            img.save(os.path.join(app.root_path, "static/uploads", filename))
            # get the image from that location
            image = os.path.join(app.config['UPLOAD_FOLDER'], filename)
           

            # load up a pre-trained model and get a prediction
            # model = pickle.load(open("ed-model/model.pkl", 'rb'))
            # d = model.predict(x)[0]

            ##############################################
            CLASS_LABELS  = ['anger', 'disgust', 'fear', 'happy', 'neutral', 'sadness', "surprise"]
            index = random.randint(0, 6)
            label = CLASS_LABELS[5]

            # finally we can render the template with the prediction and image
            return render_template('submit.html', labels=label, image = image)
        except:
            return render_template('submit.html', error=True)