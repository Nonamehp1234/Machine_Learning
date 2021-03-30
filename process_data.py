'''
    IMPORT:

        + cv2 : Use to read image (rows,cols,3) - > Convert three channels = [Blue , Green , Red].
        + np : Caculator matrix.
        + os : Irrelevant file in computer.
        + csv : Write four feature for file csv.
        + random : Applications in choose random of list.

''' 


import cv2
import numpy as np 
import os
import csv
import openpyxl
import random

# Read path file simple -> os.getcwd()
current_file = os.getcwd() +'\\' 'training_dataset\\'

# Clustering Eight Colors to Recogition
colors = ['black', 'blue', 'red', 'orange', 'yellow', 'white', 'green', 'violet']


# Open file
def open_file():

    with open('data_max.csv' , 'r') as file:
        reader = csv.reader(file)
        list = []
        for read in reader:
            list.append(read)

    return list

# Return number color . Example return number red image , blue image ,.....
def num_color(list):

    len_color = []
    i , length = 0 , 0

    for index in range(len(list)):
        if list[index][3] == colors[i]:
            length += 1
            if index == len(list) - 1:
                len_color.append(length)
        else:
            len_color.append(length)
            i += 1
            length += 1
    return len_color

# Find new cluster color : red , orange , blue , green , .... (change cluster present)
def cluster_color(list , list_data):
    
    color = []
    cluster_color = []
    for i in range(len(colors)):
        count = 0
        sum_blue , sum_green , sum_red = 0 , 0 , 0

        for j in range(len(list)):
            if list[j] == colors[i]:
                color.append(list[j])
                sum_blue += float(list_data[j][0]) 
                sum_green += float(list_data[j][1])
                sum_red += float(list_data[j][2])

        sum_blue , sum_green , sum_red = sum_blue/count , sum_green/count , sum_red/count
        cluster_color.append([sum_blue , sum_green , sum_red])

    return color , cluster_color



# Random choice one data eight colors : red , orange , violet , green
def random_data():
    list = []

    # Open file to append for list
    with open("data_max.csv" , 'r') as file:
        writer = csv.reader(file)
        for write in writer:
            list.append(write)
    
    # Count number color in file data_max.
    len_color = num_color(list)

    # Init list
    random_data_color = []

    # Take random data in file data_max
    for index in range(len(colors)):
        if index == 0:
            random_data_color.append(random.choice(list[0:len_color[index]]))
        else:
            random_data_color.append(random.choice(list[len_color[index-1]:len_color[index]]))

    # Write new file random_data.csv
    with open('random_data.csv' , 'w' , newline = '') as file:
        write = csv.writer(file)
        write.writerows(random_data_color)

    # Return list of random_data_color.
    return random_data_color


# Caculator norm p = 2 or distance Euclid.
def norm_2(list1 , list2):
    list = []

    # Algorithms distance Euclid.
    for j in range(len(list2)):
        sum = 0
        for z in range(0,3):
            sum += (int(list1[z]) - int(list2[j][z]))**2
        list.append(sum)  

    index = list.index(min(list))
    return list2[index][3]
      
        
# Return name colors of image to function self.name_color.
def color_image(image):
    for index in range(len(colors)):
        if colors[index] in image:
            return colors[index]


# Class Image - > 4 feature : Red_channels , Blue_channels , Green_channels , Name color of image reading.

# Find max histogram three channels.
class Image:

    # Create init feature of image.
    def __init__(self, path_image):
        self.name_color = color_image(path_image)
        self.path = path_image
        self.read_path_img()

    # Convert jpg or png - > matrix
    def read_path_img(self):
        image = cv2.imread(self.path)
        histogram = np.zeros((3,256), dtype = np.int64)

        '''
            Read image and give array histogram.
            histogram[0,:] -> Identisy gray 0 - > 255 (channels blue)     
            histogram[1,:] -> Identisy gray 0 - > 255 (channels green)     
            histogram[2,:] -> Identisy gray 0 - > 255 (channels red)     
        '''

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                histogram[0, image[i,j,0]] += 1
                histogram[1, image[i,j,1]] += 1
                histogram[2, image[i,j,2]] += 1

        # Return max of channel Blue
        for index in range(0,256): 
            if histogram[0][index] == max(histogram[0,:]):
                self.blue = index
                break
        
        # Return max of channel Green
        for index in range(0,256):
            if histogram[1][index] == max(histogram[1,:]):
                self.green = index
                break

        # Return max of channel Red
        for index in range(0,256):
            if histogram[2][index] == max(histogram[2,:]):
                self.red = index
                break


# Caculator Averange.
class Image_Averange:

    # Create init feature of image.
    def __init__(self, path_image):
        self.name_color = color_image(path_image)
        self.path = path_image
        self.read_path_img()

    # Convert jpg or png - > matrix
    def read_path_img(self):
        
        # Read image
        image = cv2.imread(self.path)
        histogram = np.zeros((3,256), dtype = np.int64)

        '''
            Read image and give array histogram.
            histogram[0,:] -> Identisy gray 0 - > 255 (channels blue)     
            histogram[1,:] -> Identisy gray 0 - > 255 (channels green)     
            histogram[2,:] -> Identisy gray 0 - > 255 (channels red)     
        '''

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                histogram[0, image[i,j,0]] += 1
                histogram[1, image[i,j,1]] += 1
                histogram[2, image[i,j,2]] += 1

        list = []

        # Find averange histogram three channels.
        for i in range(3):
            sum = 0
            for j in range(256):
                sum += (j+1)*histogram[i,j]
            list.append(sum/(image.shape[0]*image.shape[1]))
        
        self.blue , self.green , self.red = int(list[0]) , int(list[1]) , int(list[2])
