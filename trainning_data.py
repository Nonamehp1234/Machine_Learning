import cv2
import numpy as np 
import os

colors = ['black', 'blue', 'red', 'orange', 'yellow', 'white', 'green', 'violet']
def processing_data():
    pass

def read_image(str):
    image = cv2.imread(str)
    histogram = np.zeros((3,256), dtype = np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[0,image[i,j,0]] += 1
            histogram[1,image[i,j,1]] += 1
            histogram[2,image[i,j,2]] += 1
    for index in range(0,256):
        if histogram[0][index] == max(histogram[0,:]):
            blue = index
            break
    for index in range(0,256):
        if histogram[1][index] == max(histogram[1,:]):
            green = index
            break
    for index in range(0,256):
        if histogram[2][index] == max(histogram[2,:]):
            red = index
            break
    return blue , green , red
    # return red , green , blue
def train_data(file):
    data = []
    for index in range(len(file)):
        B , G , R = read_image(file[index])
        

def check_path_open(path_colors):
    if type(cv2.imread(path_colors + '.png')) is np.ndarray:
        return path_colors + '.png'
    elif type(cv2.imread(path_colors + '.jpg')) is np.ndarray:
        return path_colors + '.jpg'
    else:
        return False
def append_img(_path):
    file_colors = []
    for _index in range(len(colors)):
        index = 1
        path_colors = _path + colors[_index] + '\\' + colors[_index] + str(index)
        path = check_path_open(path_colors)
        if path:
            file_colors.append(path)
        while path != False:   
            index += 1
            path_colors = _path + colors[_index] + '\\' + colors[_index] + str(index)
            path = check_path_open(path_colors)
            if path:
                file_colors.append(path)
    return file_colors

if __name__ == "__main__":
    current_file = os.getcwd() +'\\' 'training_dataset\\'
    upload_img = append_img(current_file)
    data = train_data(upload_img)



'''
    Homework tomorrow :
        1. Code clean.
        2. Append function feature color . Image (B,G,R) - > what is color????
        3. Code KNN
        Complete
        
'''
