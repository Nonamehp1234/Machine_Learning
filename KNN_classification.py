import numpy as np
import csv
import process_data
import random
import heapq
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.metrics import accuracy_score
from sklearn import neighbors
from sklearn.model_selection import train_test_split


# Convert array list to array numpy.
data = np.asarray(process_data.open_file('max'))


# Train is 70 percent size data and test is 30 percent size data.
X_train, X_test, Y_train, Y_test = train_test_split(data[:, :3], data[:, 3], test_size=0.3, random_state=1)
X_train, X_test = np.array(X_train, dtype=int), np.array(X_test, dtype=int)

init_cluster = X_train[np.random.choice(X_train.shape[0], len(process_data.colors))]


# Code algorithm K-nearest-neighbor.
class Knearestneighbor:
    # Create init K - nearest - neighbors.
    def __init__(self, k_nearest=1, norm=2, random_image=False):
        self.k_nearest = k_nearest
        self.norm = norm

    # Understand x is : test data.
    def predict_Knearest(self):
        # If k_nearest == 1 => Only find distance min and end.
        if self.k_nearest == 1:
            predict = []
            for test in X_test:
                list = process_data.norm(X_train, test, self.norm)
                predict.append(Y_train[list.index(min(list))])
            # Accuracy Y_test and predict.
            print("Accuracy of 1NN: %.2f %%" % (100 * accuracy_score(Y_test, predict)))
            return 100*accuracy_score(Y_test, predict)
        elif 1 < self.k_nearest <= X_train.shape[0] and self.k_nearest % 2 != 0:
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
            return 100*accuracy_score(Y_test, predict)
        # If k_nearest > X_train.shape[0] => Not k_nearest.
        elif 1 < self.k_nearest <= X_train.shape[0] and self.k_nearest % 2 == 0:
            pass
        else:
            raise Exception('K-nearest not exceed {}.'.format(self.k_nearest))

    # Use specific realtime.
    def draw(self):
        pass


# Code algorithm K-means.
class Kmeans:

    # Create init K - means.
    def __init__(self, k_cluster=len(process_data.colors), norm=2):
        # Count K cluster include : red , green , blue , violet , black , orange , yellow , white.
        self.K_cluster = len(process_data.colors)
        # Point cluster init random.
        self.cluster = dict(zip(process_data.colors, init_cluster))
        print(self.cluster)
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
        present_color = []
        for train in X_train:
            list = process_data.norm(init_cluster, train, self.norm)
            present_color.append(process_data.colors[list.index(min(list))])

        new_color =[]
        while True:
            cluster_new = process_data.new_cluster(present_color, X_train)

            for train in X_train:
                list = process_data.norm(cluster_new, train, self.norm)
                new_color.append(process_data.colors[list.index(min(list))])

            if new_color == present_color:
                self.cluster = cluster_new
                break
            else:
                present_color = new_color

    def draw(self):
        pass


if __name__ == "__main__":
    """
    accuracy_k = []
    for i in range(len(X_train)):
        if i % 2 != 0:
            clf = Knearestneighbor(k_nearest=i, norm=2)
            accuracy_k.append(clf.predict_Knearest())
    print(accuracy_k)
    plt.plot([i for i in range(len(X_train)) if i % 2 != 0], accuracy_k)
    plt.title('Compare accuracy with k nearest neighbor')
    plt.xlabel('K-nearest-neighbor')
    plt.ylabel('Accuracy')
    plt.show()
    """
    print(X_train)
    clf = Kmeans()
    clf.algorithms_kmeans()
