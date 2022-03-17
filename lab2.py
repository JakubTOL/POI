import csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pyransac3d as pyrsc
"""
1. odczyt plikow csv \/
2. instalacja pakiety pyransac3d \/
3. znalezc rozlaczne chmury punktow za pomoca algorytmu k-srednich k=3 \/ --clusteryzacja
4. dla kazdejc chmury przeprowadzic dopaswoanie plaszczyzny za pomoca ransac
   4.1. wypisac wspolrzedne wektora normalnego do znalezionej plaszczyzny
    4.1.2 czy dana chmura jest placzczynza
    4.1.2 jesli jest to czy jest pionowa czy pozioma
"""
"""Given:
    data – A set of observations.
    model – A model to explain observed data points.
    n – Minimum number of data points required to estimate model parameters.
    k – Maximum number of iterations allowed in the algorithm.
    t – Threshold value to determine data points that are fit well by model.
    d – Number of close data points required to assert that a model fits well to data.

Return:
    bestFit – model parameters which best fit the data (or null if no good model is found)

iterations = 0
bestFit = null
bestErr = something really large

while iterations < k do
    maybeInliers := n randomly selected values from data
    maybeModel := model parameters fitted to maybeInliers
    alsoInliers := empty set
    for every point in data not in maybeInliers do
        if point fits maybeModel with an error smaller than t
             add point to alsoInliers
        end if
    end for
    if the number of elements in alsoInliers is > d then
        // This implies that we may have found a good model
        // now test how good it is.
        betterModel := model parameters fitted to all points in maybeInliers and alsoInliers
        thisErr := a measure of how well betterModel fits these points
        if thisErr < bestErr then
            bestFit := betterModel
            bestErr := thisErr
        end if
    end if
    increment iterations
end while

return bestFit"""


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
    y_pred = clusterer.fit_predict(X)  # rozpoznaj cluster i dopasuj sie do niego

    red = y_pred == 0  # jesli przydzielone do clustra 0 to czerwone
    blue = y_pred == 1
    cyan = y_pred == 2

    plt.figure()
    plt.scatter(X[red, 0], X[red, 1], c="r")
    plt.scatter(X[blue, 0], X[blue, 1], c="b")
    plt.scatter(X[cyan, 0], X[cyan, 1], c="c")
    plt.tight_layout()
    plt.show()
