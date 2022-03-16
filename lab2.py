import csv


def point_read():  # definicja funkcji
    with open('CloudPointsXY.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #next(reader)  # poiniecie naglowka
        for x, y, z in reader:  # wprowadzenie nazw naglowkow
            yield x, y, z  # odczytuj i zapamietuj wartosci z tych kolumn


points = []  # utworzenie listy
for p in point_read():
    points.append(p)  # wpisywanie wierszy do listy
    print(p)
    # points.sort()  # sortowanie listy po pierwszym elemencie kazdej krotki
    # points.sort(key=lambda x: x[n]) #sortowanie po n-tym elemencie kazdej krotki lambda jest funkcja anonimowa
points
