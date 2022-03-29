import csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
#import pyransac3d as pyrsc


def point_read_xy():  # definicja funkcji
    with open('CloudPointsCyl.xyz', newline='') as csvfile:
        # odczyt (typ pliku, separator, typ danych - tutaj zeny byly jako float)
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        # next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


def klasteryzacja_ransac():
    clusterer = KMeans(n_clusters=3)  # stworznie obiektu cluster n_cluster--- liczba clastrow
    odczyt = np.array(clusters).reshape((2000, 3))  # konwersja macierzy odczytanej 1D do 3D
    X = np.delete(odczyt, 2, axis=1)  # usun 3 kolumne czyli wspolrzedne z = 0
    y_pred = clusterer.fit_predict(X)  # rozpoznaj cluster i dopasuj sie do niego

    red = y_pred == 0  # jesli przydzielone do clustra 0 to czerwone
    blue = y_pred == 1
    cyan = y_pred == 2

    plt.figure()
    plt.scatter(X[red, 0], X[red, 1], c="r")
    plt.scatter(X[blue, 0], X[blue, 1], c="b")
    plt.scatter(X[cyan, 0], X[cyan, 1], c="c")
    plt.tight_layout()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    max_iter = 100

    for iteration in range(0, max_iter):
        # etap 1
        # wybor losowego wiersza z tablicy jako wektory
        va = odczyt[np.random.choice(odczyt.shape[0], 1, replace=False), :]
        vb = odczyt[np.random.choice(odczyt.shape[0], 1, replace=False), :]
        vc = odczyt[np.random.choice(odczyt.shape[0], 1, replace=False), :]
        vec_ua = va/np.linalg.norm(va)
        vec_ub = vb/np.linalg.norm(vb)
        vec_uc = np.cross(vec_ua, vec_ub)
        w = vec_uc
        D = -np.sum(np.multiply(w, vc))
        # print("odleglosc od 0xyz:", D)
    # etap 2
    wx = vec_uc[0]
    wy = vec_uc[1]
    wz = vec_uc[2]
    dist = [(np.abs(wx * odczyt[0] + wy * point[1] + wz * odczyt[2] + D) / np.linalg.norm(vec_uc)) for point in odczyt]

    offset = 0.3

    inliers = []
    for i in range(0, len(dist)):
        if dist[i] <= offset:
            inliers.append(i)

    print(inliers)


if __name__ == '__main__':
    clusters = []  # utworzenie listy
    for cluster in point_read_xy():
        clusters.extend(cluster)  # wpisywanie wierszy do listy
    klasteryzacja_ransac()
