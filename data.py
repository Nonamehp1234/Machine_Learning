'''
    IMPORT:

        + cv2 : Use to read image (rows,cols,3) - > Convert three channels = [Blue , Green , Red].
        + np : Caculator matrix.
        + os : Irrelevant file in computer.
        + csv : Write four feature for file csv.

''' 
import cv2
import numpy as np 
import os
import csv
import openpyxl
import process_data


# Read path file simple -> os.getcwd()
current_file = os.getcwd() +'\\' 'training_dataset\\'

# Clustering Eight Colors to Recogition
colors = ['black', 'blue', 'red', 'orange', 'yellow', 'white', 'green', 'violet']


# Check file image is : jpg or png. Not all - > return '' or ""
def check_path_open(path_colors):
    if type(cv2.imread(path_colors + '.png')) is np.ndarray:
        return path_colors + '.png'
    elif type(cv2.imread(path_colors + '.jpg')) is np.ndarray:
        return path_colors + '.jpg'
    else:
        return ""

# Write string (B,G,R,name_color) - > file excel csv.

def write_csv(feature):
    with open('data_averange.csv' , 'w' , newline = "") as file:
        write = csv.writer(file)
        write.writerows(feature)

# Read file color black - > violet

def read_file(path):
    feature = []
    for index in range(len(colors)):
        i = 1
        while path != '':
            path = check_path_open(path + colors[index] + '\\' + colors[index] + str(i))
            if path != '':
                img = process_data.Image_Averange(path)
                feature.append([str(img.blue) , str(img.green) , str(img.red) , str(img.name_color)])
                path = current_file
                i += 1

        path = current_file
        
    # Write feature -> excel csv.
    write_csv(feature)


# Function main
if __name__ == "__main__":
    read_file(current_file)