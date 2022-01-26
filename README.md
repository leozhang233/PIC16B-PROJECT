# PIC16B-PROJECT: Emotion detection using facial recognization webapp

## Abstract
Our project addresses this problem:  
**What can app developers do to improve their product given permission of camera use from the user?**  
With camera permission from the user, we could detect the user’s emotion right after they have seen our recommendation. We want to check whether the user likes or dislikes the current product, and how they feel about it. Our project focus on human facial emotions and will recommend different things to the user based on their mood. 

## Planned Deliverables
We will build a web app that contains a machine learning model to do emotion detection using facial recognition. This should be a demo or testing function for future app developers, since we will need the user to upload a selfie to check their facial emotion, instead of use build-in camera in their device to get it. With just one selfie uploaded by the user, we will be able to present different outcomes to the user, and adjust previous recommendations accordingly.   
 
The packages we planned to use are `TenserFlow` and `Flask`. The first one is for Image Classification, while the latter one is used to construct an interactive webapp. The model may be built and trained in Jupyter notebook, but will later be uploaded to our webapp.  
 
If our project is 100% successful, it should identify the user’s current mood correctly, and do a recommendation on user selected area. Then if the user doesn’t stop this process, it will ask the user to input a selfie again that represents their feeling to the previous recommendation, and adjust the follow-up recommendation accordingly.  
 
For partial success, our webapp may only be able to give recommendations in a specific area. For the modeling part, even if it may not correctly detecting the user’s emotion in some cases, we should still be able to give a general recommendation that may work for different moods.   


## Resources Required
Since our project involves emotion detection, we need to have a large data set that has many images of faces. Thankfully, we are able to find one link to this type of data set from kaggle: https://www.kaggle.com/ananthu017/emotion-detection-fer. In addition, we also plan to do some web scraping for reflection purposes. For example, scraping some videos/images/quotes to make users feel more positive based on their current mood (If the users are feeling sad, our system will automatically send something funny as a response; if the users are feeling angry, our system will automatically send something relaxing as a response). Therefore, we still need one or more resources to help us achieve this goal.

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

## What You Will Learn
By completing this project, we are able to learn how to train a TensorFlow model to categorize each face based on the emotion shown in the facial expression in one of the categories, such as happy, unhappy, neutral, and so forth. After we finish optimizing this machine learning model, we will learn how to transfer this functionality to a visually rich webapp while introducing user interaction features and applying real-time web scraping techniques. Last but not least, every member of our team will learn how to work with others and handle issues that only arise in groups. In the end, all of us will develop strong teamwork skills.

## Risks
Firstly, we might not have the ability to adjust the selfie inputted by the user. For example, if the selfie does not fall in certain criteria,  it might lead to unsuccessfully recognization. The size, color, and format of the input might also affect our outcome. Then it may require slightly more complicated skills in Webapp building and input processing, which we don’t currently have.  
 
Another risky thing that could potentially stop us from achieving the full deliverable above is that our recommendation system may not work. Since our main focus in the project is facial emotion detection, we might have a recommendation pool with a limited size. That is, all our recommendations are built-in set up to deal with a certain mood, and they may only be available for a specific topic chosen by us due to size and technical limitations. It may also not reflect the latest changes, for example,  recommending the latest movie to watch.  
 
## Ethics
The major assumption for our project is we are having the user's permission to use their device camera and analyze the data we have collected. Consumers should always be able to decide whether they want their data used in a certain way.   

However, there might be some potential ethics problems with our facial emotion classification models. For example, the algorithmic bias. According to the researchers, facial recognition technologies falsely identified Black and Asian faces 10 to 100 times more often than they did white faces. The technologies also falsely identified women more than they did men—making Black women particularly vulnerable to algorithmic bias. That may be due to the limitation and facial data availability of the training data. The original training dataset might be skewed and collected from an unbalanced population with a larger proportion of white faces.  Even if developers can make the algorithms equitable, the technology may be unintentionally employed in a discriminatory manner, disproportionately harming marginalized populations. This is so crucial that we definitely need to be aware of. We will try our best to make our dataset as diverse as possible to minimize this unpleased effect.  

## Who will benefit from this project?
If our model eventually becomes mature enough and is able to detect more subtle emotions (not just extreme emotions like happy and sad), then it can be a great benefit to most app owners and developers to potentially learn about user preferences and ways to improve their apps. Provided that the app owner successfully asked for access to camera, they might be able to use emotion detection along with the data about current actions of the user on their apps (eg. clicking into, staying on, or closing a page) to understand user preferences. For instance, if a user keeps frowning and stays on a certain page for quite a long time, it might be that something confusing is happening on that page. This app might also be used in IoT (Internet of Things) in the future when household appliances are intelligent and can personalize behavior according to user emotions they detect.

Assuming this project will help improve user experience, this project will also benefit the target customers because they get to use a better product.

## Who might be harmed by this project?
We have mentioned that this project is helpful only when it is lawfully used. For example, in order to protect user privacy, the app owner should only stores the information about detected emotion (eg. happy, sad, confused, angry) and match with user activity using something like user ID, without actually keeping the photos of their users without permission. This also means that if the app owners trace user information without permission, or if this model is used in some other activities against the law, then this technology can actually hurt privacy. I believe finding a balance between technical development and user privacy is an ongoing question faced by the entire tech industry. 

Also, if the data we used to train the models is skewed due to some historically inherent reasons, then the model might work better on one group than another, which might lead to certain social/racial biases, but this is left to explore.

## Will the world become an overall better place because of the existence of our product? 
Similar to what we mentioned above, under the assumptions that a. The usage of this model is lawful b. The model is mature enough to successfully detect more subtle emotions, then this model will help optimize people’s experience regarding many products and thus improve quality of life, which can make the world an overall better place.

## Tentative timeline
- After 2 weeks:
    We will have constructed the structure of our webapp, and developed the logic that we will be using for user interaction. We will also have chosen and cleaned the dataset needed to train our model.

- After 4 weeks:
    We will have developed trained our model with the preprocessed data, and will have made attempts to optimize model functionality.

- After 6 weeks:
    We will have combined the model with our webapp to finalize the product, and will have performed several tests to see if the model works well with our interactive logic developed in the first two weeks.
