import csv


def point_readXY():  # definicja funkcji
    with open('CloudPointsXY.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


pointsXY = []  # utworzenie listy
for p in point_readXY():
    pointsXY.append(p)  # wpisywanie wierszy do listy
    print(p)
    # points.sort()  # sortowanie listy po pierwszym elemencie kazdej krotki
    # points.sort(key=lambda x: x[n]) #sortowanie po n-tym elemencie kazdej krotki lambda jest funkcja anonimowa
pointsXY

def point_readXZ():  # definicja funkcji
    with open('CloudPointsXZ.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


pointsXZ = []  # utworzenie listy
for p in point_readXZ():
    pointsXZ.append(p)  # wpisywanie wierszy do listy
    print(p)
pointsXZ


def point_readCyl():  # definicja funkcji
    with open('CloudPointsCyl.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #next(reader)  # pominiecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


pointsCyl = []  # utworzenie listy
for p in point_readCyl():
    pointsCyl.append(p)  # wpisywanie wierszy do listy
    print(p)
pointsCyl
