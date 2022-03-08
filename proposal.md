## Abstract
Our project will try to find an answer to the following question:  
**Given permission of camera access, what information can we obtain from facial recognition and how can we potentially make use of that information?**
Overall, our project will focus on facial emotion recognition and recommendations based on the detected emotion. More specifically, we will train a model that is able to classify the emotion of face deteched in an uploaded photo, and make the whole process interactive through implementation on our webpage.
 
## Planned Deliverables
We will build a web app that contains a machine learning model to do emotion detection using facial recognition. This should be a demo or a testing function for future app developers, since we will need the user to upload a selfie themselves instead of using the build-in camera to capture the user's facial expressions. With just one selfie uploaded by the user, we will be able to present different outcomes to the user according to the deteched emotion.   
 
The main packages we use are `TenserFlow` and `Flask`. The first one is for Image Classification, while the second one is used to construct an interactive webapp. The model may be built and trained in Jupyter notebook, but will later be uploaded to our webapp.  
 
For full success, after a user uploads an image, our model should be able to automatically crop the photo by finding the human face in the photo, identify the user’s current mood correctlym and provide the user with a video recommendation on our webapp. 
 
For partial success, our webapp may only be able to roughly identify the user's current mood and make a recommendation that is not so precise. Also the model might not be able to crop the photo in a smart way as we planned.


## Resources Required
Since our project involves emotion detection, we need to have a large data set that has many images of faces. Thankfully, we are able to find one link to this type of data set from kaggle: https://www.kaggle.com/ananthu017/emotion-detection-fer. In addition, we also plan to do some web scraping for reflection purposes. Since the page structure for YouTube search page is highly complex and basic scraping does not work very well, we will make use of some webscraping packages that will become handy when scraping information from YouTube. Still, we need to write our own codes for the actual scraping process.


## Tools and Skills Required
The tools and skills we required are:
- TensorFlow (machine learning)
- Sqlite3 (database connection, SQL command)
- Flask (developing web app)
- Scrapy (web scraping)
- Matplotlib/Seaborn/Plotly (data visualization)
- Sklearn (preprocessing, confusion matrix, etc.)
- Pandas + Numpy (data analysis)
- GitHub (software collaboration)
- OpenCV (Face Recognition)

How we trained the machine learning model with Tensorflow InceptionV3 can be found [here](https://www.kaggle.com/jadenwsr/emotion-detection-with-inceptionv3/notebook).

## What You Will Learn
By completing this project, we will learn how to use OpenCV to do facial recognition, train a TensorFlow model to categorize each face based on the emotion shown in the facial expression in one of the categories, such as happy, unhappy, neutral, and so forth. After we finish optimizing this machine learning model, we will learn how to transfer this functionality to a visually rich webapp. We will also learn how to extract information from more complex websites. Last but not least, every member of our team will learn how to work with others and handle issues that only arise in groups. In the end, all of us will develop strong teamwork skills.

## Risks
Firstly, we assume that the image uploaded by the user is "correct" in the sense that it can be understood by our model. For example, if the photo is blurry or contains multiple faces (or even no faces), it might lead to unsuccessfully recognization. The size, color, and format of the input might also affect our outcome. Then it may require slightly more complicated skills in webapp building and input processing, which we don’t currently have.  
 
Another risky thing that could potentially stop us from achieving the full deliverable above is that our recommendation system may not work so well. Since our main focus in the project is facial emotion detection, we might have a recommendation pool with a limited size. That is, all our recommendations are built-in with a static database, so they may only be available for a specific topic chosen by us due to size and technical limitations. It may also not reflect the latest changes, for example, recommending the latest movie or the recent most popular videos for the user to watch.  
 
## Ethics
For simple webapp implementation, the image upload is totally voluntary. But if similar projects are used in actual apps, one major assumption for our project is that we are having the user's permission to use their device camera and analyze the data we have collected. Users should always be informed that we are trying to access the camera, and they should always be able to decide whether they want their data used in a certain way.   

However, there might be some potential ethics problems with our facial emotion classification models. One example is algorithmic bias as a result of historical biases or imbalanced data collection. According to relevant news and research, facial recognition technologies falsely identified Black and Asian faces 10 to 100 times more often than they did white faces. The technologies also falsely identified women more than they did men—making Black women particularly vulnerable to algorithmic bias. That may be due to the limitation and facial data availability of the training data. The original training dataset might be skewed and collected from an unbalanced population with a larger proportion of white faces.  Even if developers can make the algorithms equitable, the technology may be unintentionally employed in a discriminatory manner, disproportionately harming marginalized populations. This is so crucial that we definitely need to be aware of. We will try our best to make our dataset as diverse as possible to minimize this unpleased effect.  

## Who will benefit from this project?
Currently, our webapp can potentially help users with negative emotions to feel better because of our recommended videos. In later stages, if our model eventually becomes mature enough and is able to detect more subtle emotions (not just extreme emotions like happy and sad), then it can be a great benefit to most app owners and developers to potentially learn about user preferences, thus able to better improve their app. Provided that the app owner successfully asked for access to camera, they might be able to use emotion detection along with the data about current actions of the user on their apps (eg. clicking into, staying on, or closing a page) to understand user preferences. For instance, if a user keeps frowning and stays on one page for a long time, it can be that something confusing is happening on that page. This app might also be used in IoT (Internet of Things) in the future when household appliances are intelligent and can personalize behavior according to user emotions they detect.

Assuming this project will help improve user experience, it will also eventually benefit the target customers because they get to use a better product.

## Who might be harmed by this project?
At our current level, users might be lightly harmed if we incorrectly identify their emotion and recommended videos that they don't like. If the project is implemented on actual apps, then a serious problems is whether it is lawfully used. For example, in order to protect user privacy, the app owner should only stores the information about detected emotion (eg. happy, sad, confused, angry) and match with user activity using something like user ID, without actually keeping the photos of their users without permission. This also means that if the app owners trace user information without permission, or if this model is used in some other activities against the law, then this technology can actually hurt privacy. I believe finding a balance between technical development and user privacy is an ongoing question faced by the entire tech industry. 

Also, if the data we used to train the models is skewed due to some historically inherent reasons, then the model might work better on one group than another, which might lead to certain social/racial biases, but this is left to explore.

## Will the world become an overall better place because of the existence of our product? 
Similar to what we mentioned above, under the assumptions that 1. The usage of this model is lawful 2. The model is mature enough to successfully detect more subtle emotions, then this model will help optimize people’s experience regarding many products and thus improve quality of life, which can make the world an overall better place.

## Tentative timeline
- After 2 weeks:
    We will have constructed the structure of our webapp, and developed the logic that we will be using for user interaction. We will also have chosen and cleaned the dataset needed to train our model.

- After 4 weeks:
    We will have developed trained our model with the preprocessed data, and will have made attempts to optimize model functionality.

- After 6 weeks:
    We will have combined the model with our webapp to finalize the product, and will have performed several tests to see if the model works well with our interactive logic developed in the first two weeks.
