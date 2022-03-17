import csv
from sklearn.cluster import KMeans
from scipy.stats import norm
import pyransac3d as pyrsc
import matplotlib.pyplot as plt
import numpy as np
"""
1. odczyt plikow csv \/
2. instalacja pakiety pyransac3d \/
3. znalezc rozlaczne chmury punktow za pomoca algorytmu k-srednich k=3 \/ --clusteryzacja
4. dla kazdejc chmury przeprowadzic dopaswoanie plaszczyzny za pomoca ransac
   4.1. wypisac wspolrzedne wektora normalnego do znalezionej plaszczyzny
    4.1.2 czy dana chmura jest placzczynza
    4.1.2 jesli jest to czy jest pionowa czy pozioma
"""


def point_read_xy():  # definicja funkcji
    with open('CloudPointsXY.xyz', newline='') as csvfile:
        # odczyt (typ pliku, separator, typ danych - tutaj zeny byly jako float)
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        # next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


if __name__ == '__main__':
    clusters = []  # utworzenie listy
    for cluster in point_read_xy():
        clusters.extend(cluster)  # wpisywanie wierszy do listy

    clusterer = KMeans(n_clusters=3)  # stworznie obiektu cluster n_cluster--- liczba clastrow
    X = np.array(clusters).reshape((2000, 3))  # konwersja macierzy odczytanej 1D do 3D
    X = np.delete(X, 2, axis=1)  # usun 3 kolumne czyli wspolrzedne z = 0
    print(X)
    y_pred = clusterer.fit_predict(X)  # rozpoznaj cluster i dopasuj sie do niego

    red = y_pred == 0  # jesli przydzielone do clustra 0 to czerwone
    blue = y_pred == 1
    cyan = y_pred == 2

    plt.figure()
    plt.scatter(X[red, 0], X[red, 1], c="r")
    plt.scatter(X[blue, 0], X[blue, 1], c="b")
    plt.scatter(X[cyan, 0], X[cyan, 1], c="c")
    # plt.tight_layout()
    plt.show()
