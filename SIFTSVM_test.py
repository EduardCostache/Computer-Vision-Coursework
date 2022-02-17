"""
Created on Sun Aug 22 21:37:51 2021

@author: Edward

The following code was implemented from the tutorial with minor adjustsments made by me.
"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from skimage import img_as_ubyte, io, color
from joblib import load
from sklearn import metrics
from sklearn.utils import shuffle

test_path = 'Personal_Dataset'
model = 'SIFT-SVM.joblib'

def EmotionRecognition(path_to_testset, model):
    X, y = get_data(path_to_testset)
    X, y = shuffle(X, y)
    
    clf, k, kmeans = load(model)
    sift = cv2.SIFT.create()
    
    hist_list = []
    
    for i in range(len(X)):
        img = img_as_ubyte(color.rgb2gray(X[i]))
        kp, des = sift.detectAndCompute(img, None)

        if des is not None:
            hist = np.zeros(k)

            idx = kmeans.predict(des)

            for j in idx:
                hist[j] = hist[j] + (1 / len(des))

            hist_list.append(hist)

        else:
            hist_list.append(None)
        
    #Remove potential cases of images with no descriptors
    idx_not_empty = [i for i, x in enumerate(hist_list) if x is not None]
    hist_list = [hist_list[i] for i in idx_not_empty]
    y = [y[i] for i in idx_not_empty]
    hist_array = np.vstack(hist_list)

    predicted = clf.predict(hist_array).tolist()
    
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


EmotionRecognition(test_path, model)



