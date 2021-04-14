import numpy as np
import csv
import process_data
import random
import heapq
from collections import Counter
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# Convert array list to array numpy.
data = np.asarray(process_data.open_file('max'))

# Train is 70 percent size data and test is 30 percent size data.
X_train, X_test, Y_train, Y_test = train_test_split(data[:, :3], data[:, 3], test_size=0.3, random_state=1)
X_train, X_test = np.array(X_train, dtype=int), np.array(X_test, dtype=int)


# Code algorithm K-nearest-neighbor.
class Knearestneighbor:
    # Create init K - nearest - neighbors.
    def __init__(self, k_nearest=1, norm=2, random_image=False):
        self.k_nearest = k_nearest
        self.norm = norm

    # Understand x is : test data.
    def predict_Knearest(self):
        if self.k_nearest == 1:
            predict = []
            for test in X_test:
                list = process_data.norm(X_train, test, self.norm)
                predict.append(Y_train[list.index(min(list))])
            print("Accuracy of 1NN: %.2f %%" % (100 * accuracy_score(Y_test, predict)))
            del predict
        elif 1 < self.k_nearest <= X_train.shape[0]:
            predict = []
            for test in X_test:
                list_color = []
                list = process_data.norm(X_train, test, self.norm)
                for iteration in range(self.k_nearest):
                    list_color.append(Y_train[list.index(min(list))])
                    list[list.index(min(list))] = max(list)
                predict.append(max(list_color, key=list_color.count))
                del list_color
            print("Accuracy of {0}NN: {1} %%".format(self.k_nearest, (100 * accuracy_score(Y_test, predict))))
            del predict
        else:
            raise Exception('K-nearest not exceed {}.'.format(self.k_nearest))

    # Use specific realtime.
    def use(self):
        pass


# Code algorithm K-means.
class Kmeans:

    # Create init K - means.
    def __init__(self, k_cluster=len(process_data.colors), norm=2):
        # Count K cluster include : red , green , blue , violet , black , orange , yellow , white.
        self.K_cluster = len(process_data.colors)
        # Point cluster init random.
        self.cluster = X_train[np.random.choice(X_train.shape[0], self.K_cluster)]
        self.norm = norm

    # Implement algorithms K - means.
    def algorithms_kmeans(self):
        """
          Step 1 : init k cluster -> Finished.
          Step 2 : Calculator distance between two data points with three parameters :
          + Blue channels.
          + Green channels.
          + Red channels.
        """
        present = []
        for train in X_train:
            present.append(process_data.norm(cluster, train, self.norm))
        present = np.asarray(present)
        _, index = np.unique(present, return_counts=True)
        while True:
            pass


if __name__ == "__main__":
    clf = Knearestneighbor(k_nearest=1, norm=2)
    _clf = Knearestneighbor(k_nearest=5, norm=2)
    print(clf.predict_Knearest())
