# PIC16B-PROJECT: Emotion detection using facial recognization webapp

## Team member from Group (BGS)

- [Jiaqi Li](https://github.com/jqlaura)
- [Shurui Wang](https://github.com/JadenWSR)
- [Yi Zhang](https://github.com/leozhang233)

## How to run this app on your computer from command line
 At the command prompt or terminal, navigate to your projects directory
- Mac: $ export FLASK_ENV=development; flask run
- Windows: set FLASK_ENV=development; flask run

Site will be available at: http://localhost:5000

Note:

- Please make sure you have installed the required versions of all python packages needed in [requirements.txt](https://github.com/leozhang233/PIC16B-PROJECT/blob/main/requirements.txt) before you run the app.
- If you have encountered this error: **AssertionError: Duplicate registrations for type 'experimentalOptimizer'**, please uninstall keras, tensorboard, tensorflow, tensorflow-gpu if it's installed, tb-nightly, keras-nightly, tf-nightly from your computer, then re-install them all and try again.


## Webapp overview
To briefly explain what our Webapp does, it contains a machine learning model for emotion detection using facial recognition and provide some recommendations to our users.
This webapp should be a demo or a testing function for future app developers, since we will need the user to upload a selfie themselves instead of using the build-in camera to capture the user's facial expressions. With just one selfie uploaded by the user, we will be able to present different outcomes to the user according to the deteched emotion.

In order to make the whole process interactive, our webapp asks the user to submit a selfie of themselves, and the built-in model will recognize their emotion in the photo and make a recommendation accordingly. Now I will introduce the detailed functions of our webapp.



## Demonstration of webapp functionality
On the main page we have our project overview that specifies what will be achieved in this project. This part is basically the same as our project proposal, used to give the user a sense of what the app is doing.

![main_page.png](/images/main_page.png)

 Next, we have an upload page with detailed instructions regarding what kind of photo the machine is able to recognize (check out the image below). The user can simply click the upload button named "Choose File" to submit a local file from their computer. After selecting the file, the user should click "Upload Image" and let the machine recognize the face in the photo.
 
![upload.png](/images/upload.png)

To allow more flexibility, we also design a "smart cropping" function so that if the image submitted is not ideal, we try out best to recognize the face shown in the photo. For instance, if the face is too small or if it’s not in the middle of the photo, our model will automatically locate the face and then crop the photo accordingly, as you can see in the image below:

![crop.png](/images/crop.png)
  
In addition ,our model is also able to handle the case where there are multiple faces in the photo. In this case, the model will randomly locate a face that it successfully find and then move on to detect emotion. If you like, you may want to try uploading a photo and see the result yourself!

![multiple_faces.png](/images/multiple_faces.png)

After successfully finding a face, our model will first let the user know the result of the prediction (ie. a line saying "Looks like you feel happy!"), and then ask the user whether the prediction is predict in the user's opinion. It will also provide the user with several recommendations in the form of either a quote, a video, or both, using the prediction given by our embedded facial recognition machine. However, the recommended content will not display automatically: the user can select whether they want to see this recommendation or not. The quotes are extracted from one of the largest quotation websites using web scraping. Similarly, the video comes from our database which contains over 2000 youtube videos classified into several categories, each of which is specifically designed to be recommended to a certain emotion. 


As you can see, users are allowed to select:
- 1. whether they think the result is correct
- 2. whether they want a certain recommendation.
The user is also free to leave a comment to improve our app if they have any specific ideas they want to share. Now we will examine what will happen in each case.

![demo.png](/images/demo.png)

### Case I. Quotation 
If the user decides to see the recommended quote, they can click on the "Yes, I want to receive a quotation" choice and click "submit". Then the user will be taken to the page which includes the quotation we suggested for the user based on the detected emotion.
It is possible for the user to click "Start Again" and restart the whole photo uploade and recognition process.

![quote.png](/images/quote.png)

### Case II. Video 
If the user decides to see the recommended YouTube video, they can click on the "Yes, I want to receive a video" choice and click "submit". Then the user will be taken to the page which includes the YouTube video from our video database that we suggested for the user based on the detected emotion.
Similarly, it is possible for the user to click "Start Again" and restart the whole photo uploade and recognition process as well.

![video.png](/images/video.png)

### Case III. Recommendation Failed
This is a specific case that we've described in our project presentation and proposal, that when the face is detected as neutral, we won't be able to give any recommendation. In this case, the user is only allowed to either let us know the result is correct, or leave a comment/feedback.

![neutral.png](/images/neutral.png)

### Case III. Feedback
Suppose the user disagrees with our prediction: it can either be that the prediction is indeed wrong, or that the user wants to share their point of view. Then we will allow the user to leave a feedback to us for our future model improvement. As you can see below, the user will be taken to our feedback page if they choose the "feedback" option on the result page. Also, if the user does not leave their name, it's fine: the webapp will mark the user as anonymous. You may also click the pink "summary" button to see five randomly chosen past feedbacks, previously written by some other users, that we stored on the website.

![feedback.png](/images/feedback.png)

### Restrictions and limits
Since our webapp is not mature enough, there are many places in which we could make further improvements. Although we like the blue and gold coloring which correspond to the colors of UCLA, we believe that aesthetics is something that can definitely be improved if given more time. Also, our app does not take into consideration the case when the photo submitted has no face in it. In the future, we should probably design the webapp so that it gives further instructions when the user submit an unacceptable image. One more thing to notice is that when the face is deteched neutral, our webapp can do nothing actually meaningful, because we haven't come up with an idea of what content to recommend in this specific case. 
At last, I would like to point out that although the contents in the database are scraped from the internet using webscraping, the keywords we used for scraping (or the logic behind all the codings) are subjective, so the accuracy or properness of the recommended content remains to be a potential problem. In the future, we believe all the potential drawbacks we described can either be mitigated or eliminated. 

This is the end of our webapp demonstration. Thank you for using our webapp!
