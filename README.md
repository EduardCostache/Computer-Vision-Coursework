# Facial-Emotion--Recognition-Pipeline
## Description
I have trained and tested 3 different image classification models consisting of a feature-descriptor and classifier pair. It is important to note that
the accuracy of these models depends on the amount of data that was available. Hence, the accuracy of the models are above average, see the report for
detailed information.


Also a video is provided for further information: https://youtu.be/wk7kKhNAhB8

## How to use
First you will need a set of images, and for that i have provided my own personal dataset which is already formatted for the models. By formatting i mean that
each folder must be labeled by emotion with images displaying said emotions. If you are going to use your own dataset, make use of the data_handler.py file
which provides methoods for formatting your dataset.

To test a model you simply need to run the MODEL_NAME.py file, preferably in an IDE such as Spyder.
