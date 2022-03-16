import csv
import pyransac3d as pyrsc
"""
1. odczyt plikow csv \/
2. instalacja pakiety pyransac3d \/
3. znalezc rozlaczne chmury punktow za pomoca algorytmu k-srednich k=3 ???
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


pointsXY = []  # utworzenie listy
for p in point_read_xy():
    pointsXY.append(p)  # wpisywanie wierszy do listy
    print(p)
    # points.sort()  # sortowanie listy po pierwszym elemencie kazdej krotki
    # points.sort(key=lambda x: x[n]) #sortowanie po n-tym elemencie kazdej krotki lambda jest funkcja anonimowa
pointsXY


def point_read_xz():  # definicja funkcji
    with open('CloudPointsXZ.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


pointsXZ = []  # utworzenie listy
for p in point_read_xz():
    pointsXZ.append(p)  # wpisywanie wierszy do listy
    print(p)
pointsXZ


def point_read_cyl():  # definicja funkcji
    with open('CloudPointsCyl.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


pointsCyl = []  # utworzenie listy
for p in point_read_cyl():
    pointsCyl.append(p)  # wpisywanie wierszy do listy
    print(p)
pointsCyl
