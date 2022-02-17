"""

Made to sort the data into folers based on their labels and also to balance the dataset.

@Author Edward

The following code was all written by me

"""

import os
import shutil
from collections import Counter
import random

path = 'CW_Dataset_test2/train'
path_test = 'CW_Dataset_test2/test'
label_path = 'CW_Dataset_base/labels/list_label_train.txt'

def sort_img_to_label_folders(folder_path, label_path):
    label_file = open(label_path, 'r')
    lines = list(label_file)
    label_file.close()
  
    file_names = [file for file in os.listdir(path) if file.endswith('.jpg')]
    labels = [line.split()[1] for line in lines]

    for i, file in enumerate(file_names):
        file_path = os.path.join(path, file)
        if(labels[i] == '1'):
            shutil.move(file_path, os.path.join(path, '1'))
        if(labels[i] == '2'):
            shutil.move(file_path, os.path.join(path, '2'))
        if(labels[i] == '3'):
            shutil.move(file_path, os.path.join(path, '3'))
        if(labels[i] == '4'):
            shutil.move(file_path, os.path.join(path, '4'))
        if(labels[i] == '5'):
            shutil.move(file_path, os.path.join(path, '5'))
        if(labels[i] == '6'):
            shutil.move(file_path, os.path.join(path, '6'))
        if(labels[i] == '7'):
            shutil.move(file_path, os.path.join(path, '7'))


def count_data(folder_path):
    print("Fetching data...")
    labels = []
    folder_names = [folder for folder in sorted(os.listdir(folder_path)) if not folder.startswith('.')]
    counter = 0
    
    for folder in folder_names:
        file_names = [file for file in sorted(os.listdir(os.path.join(folder_path, folder))) if file.endswith('.jpg')]
        for file in file_names:    
            labels.append(folder)
            counter+=1
    
    print("Done!")
    print(Counter(labels))
    print(counter)
    
    
def sample_data_equally(target, folder_path):
    
    folder_names = [folder for folder in sorted(os.listdir(folder_path)) if not folder.startswith('.')]

    for folder in folder_names:
        file_names = [file for file in sorted(os.listdir(os.path.join(folder_path, folder))) if file.endswith('.jpg')]
        copy_counter = 1
        
        if len(file_names) > target:                   #Random Undersampling
            while len(os.listdir(os.path.join(folder_path, folder))) > target:
                random_file = random.choice(file_names)
                os.remove(os.path.join(folder_path, folder, random_file))
                file_names.remove(random_file)
        else:                                               #Random Oversmapling
            while len(os.listdir(os.path.join(folder_path, folder))) < target:
                random_file = random.choice(file_names)
                shutil.copyfile(os.path.join(folder_path, folder, random_file), os.path.join(folder_path, folder, 'copy{counter}.jpg'.format(counter = copy_counter)) )
                copy_counter += 1
            
def count_data_without_format(labels_path):
    file = open(labels_path, 'r')
    lines = list(file)
    labels = []
    
    for line in lines:
        labels.append(line.split()[1])
    
    return labels

lines = count_data_without_format(label_path)
print(Counter(lines))





















