# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request

import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pickle
import random

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io
import base64


# Create web app, run with flask run
# (set "FLASK_ENV" variable to "development" first!!!)

app = Flask(__name__)

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
            img = request.files['image']
            # img = np.loadtxt(img)
            
            # reshape into appropriate format for prediction
            # x = img.reshape(8, 8)
            
            # load up a pre-trained model and get a prediction
            # model = pickle.load(open("ed-model/model.pkl", 'rb'))
            # d = model.predict(x)[0]

            ##############################################
            CLASS_LABELS  = ['anger', 'disgust', 'fear', 'happy', 'neutral', 'sadness', "surprise"]
            index = random.randint(0, 6)
            label = CLASS_LABELS[index]

            # plot the image itself
            # fig = Figure(figsize = (3, 3))
            # ax = fig.add_subplot(1, 1, 1,)
            # ax.imshow(img, cmap = "binary")
            # ax.axis("off")
            
            # in order to show the plot on flask, we need to do a few tricks
            # Convert plot to PNG image
            # need to: 
            # import io 
            # import base64 
            # pngImage = io.BytesIO()
            # FigureCanvas(fig).print_png(pngImage)
            
            # Encode PNG image to base64 string
            # pngImageB64String = "data:image/png;base64,"
            # pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
            
            # finally we can render the template with the prediction and image
            return render_template('submit.html', labels=label, image=img)
        except:
            return render_template('submit.html', error=True)