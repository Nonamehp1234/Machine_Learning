import numpy as np
import csv
import process_data
import random

# Code algorithm K-nearest-neighbor.
'''
def predict_color(list):
    index = list.index(min(list))
    return index


def distance_Euclid(img , data_store):
    sum = 0
    list = []
    for index in range(len(data_store)):
        sum += (int(data_store[index][0]) - img.blue)**2 + (int(data_store[index][1]) - img.green)**2 + (int(data_store[index][2]) - img.red)**2 
        list.append(sum)
        sum = 0
    _index = predict_color(list)
    print(data_store[_index][3])
'''

# Code algorithm K-means.
class K_means:
    def __init__(self):
        super().__init__()

    

def open_data():
    list = []
    with open("data_max.csv" , 'r') as file:
        writer = csv.reader(file)
        for write in writer:
            list.append(write)
    return list



if __name__ == "__main__":
    list_data = open_data()
    len_color = process_data.num_color(list_data)
    print(len_color)  
