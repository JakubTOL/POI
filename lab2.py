import csv
from sklearn.cluster import KMeans
from scipy.stats import norm
import pyransac3d as pyrsc
import matplotlib.pyplot as plt
import numpy as np
"""
1. odczyt plikow csv \/
2. instalacja pakiety pyransac3d \/
3. znalezc rozlaczne chmury punktow za pomoca algorytmu k-srednich k=3 ??? --clusteryzacja?
4. dla kazdejc chmury przeprowadzic dopaswoanie plaszczyzny za pomoca ransac
   4.1. wypisac wspolrzedne wektora normalnego do znalezionej plaszczyzny
    4.1.2 czy dana chmura jest placzczynza
    4.1.2 jesli jest to czy jest pionowa czy pozioma
"""


def point_read_xy():  # definicja funkcji
    with open('CloudPointsXY.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


if __name__ == '__main__':
    pointsXY = []  # utworzenie listy
    for p in point_read_xy():
        pointsXY.append(p)  # wpisywanie wierszy do listy
        # print(p)
        # pointsXY.sort()  # sortowanie listy po pierwszym elemencie kazdej krotki
        # points.sort(key=lambda x: x[n]) #sortowanie po n-tym elemencie kazdej krotki lambda jest funkcja anonimowa
    x1, y1, z1 = zip(*pointsXY)  # wydziel wartosci z tablicy pointsXY
    # print(x1)
# TRZEBA WARTOSCI WYDZIELIC NA KOLUMNY !!!!!
    plt.figure()
    plt.ylabel('x', fontsize=12)
    plt.xlabel('y', fontsize=12)
    plt.tight_layout()
    plt.scatter(x1, y1)
    plt.show()

"""def point_read_xz():  # definicja funkcji
    with open('CloudPointsXZ.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


pointsXZ = []  # utworzenie listy
for p in point_read_xz():
    pointsXZ.append(p)  # wpisywanie wierszy do listy


def point_read_cyl():  # definicja funkcji
    with open('CloudPointsCyl.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


pointsCyl = []  # utworzenie listy
for p in point_read_cyl():
    pointsCyl.append(p)  # wpisywanie wierszy do listy"""

"""cluster = KMeans(n_clusters=3)  # stworznie obiektu cluster n_cluster--- liczba clastrow
X = np.array(clusters)
cluster.fit(X)
y_pred = cluster.fit_predict(X)  # rozpoznaj cluster i dopasuj sie do niego"""
