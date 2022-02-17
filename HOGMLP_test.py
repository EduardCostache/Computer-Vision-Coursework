"""
Created on Mon Aug 23 22:25:57 2021

@author: Edward

The following code was implemented from the tutorial with minor adjustsments made by me.
"""

import os
from matplotlib import pyplot as plt
from skimage import img_as_ubyte, io, color
from skimage.feature import hog
from sklearn import metrics
from joblib import load
from sklearn.utils import shuffle

test_path = 'Personal_Dataset'

def EmotionRecognition(path_to_testset, model_type='HOG-MLP'):
    X, y = get_data(path_to_testset)
    X, y = shuffle(X, y)
    
    clf = load('HOG-MLP.joblib')
    
    hog_features_test = []
    
    for image in X:
        image = img_as_ubyte(color.rgb2gray(image))
        fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),cells_per_block=(1, 1), visualize=True)
        hog_features_test.append(fd)
        
    predicted = clf.predict(hog_features_test)
    
    fig, axes = plt.subplots(2, 5, figsize=(14, 7), sharex=True, sharey=True)
    ax = axes.ravel()

    for i in range(10):
        ax[i].imshow(X[i])
        ax[i].set_title(f'Label: {y[i]} \n Prediction: {predicted[i]}')
        ax[i].set_axis_off()
    fig.tight_layout()
    plt.show()
    
    print(f"""Classification report for classifier {clf}:{metrics.classification_report(y, predicted)}\n""")
    print("Done! End of Program.")

def get_data(folder_path):
    print("Fetching data...")
    images = []
    labels = []
    folder_names = [folder for folder in sorted(os.listdir(folder_path)) if not folder.startswith('.')]
    
    for folder in folder_names:
        file_names = [file for file in sorted(os.listdir(os.path.join(folder_path, folder))) if file.endswith('.jpg')]
        for file in file_names:    
            images.append(io.imread(os.path.join(folder_path, folder, file)))
            labels.append(folder)
    
    print("Done!")
    return images, labels

EmotionRecognition(test_path)
