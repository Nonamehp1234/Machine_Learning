import numpy as np
import csv
import process_data
import random

# Code algorithm K-nearest-neighbor.
class K_nearest_neighbor:
    def __init__(self):
        super().__init__()


def predict_color(list):
    index = list.index(min(list))
    return index

'''
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

    # Create init K - Cluster ( K : number color find )
    def __init__(self):

        list = []
        with open('random_data.csv' , 'r') as file:
            writer = csv.reader(file)
            for index in writer:
                list.append(index)

        self.cluster = list


    # Check color previous and after have change
    def check(self , colors_new , colors_present):
        return (colors_new == colors_present)


    # Run algorithms K - means.
    def algorithm(self):

        list_data = process_data.open_file()
        colors_present = []
        colors_new = []
        
        while check(colors_new , colors_present) != True:

            if len(colors_present) == 0:
                for index in range(len(list_data)):
                    colors_present.append(process_data.norm_2(list_data[index] , self.cluster))

            present , cluster_new = process_data.cluster_color(colors_present , list_data)        




if __name__ == "__main__":
    problem = K_means()
    problem.algorithm()
    
