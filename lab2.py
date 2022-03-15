import csv


def planet_reader():  # definicja funkcji
    with open('planets.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # poiniecie naglowka
        for name, seq, radius, mass in reader:  # wprowadzenie nazw naglowkow
            yield (name, int(seq), int(radius), float(mass))  # odczytuj i zapamietuj wartosci z tych kolumn


planets = []  # utworzenie listy
for p in planet_reader():
    planets.append(p)  # wpisywanie wierszy do listy

planets.sort()  # sortowanie listy po pierwszym elemencie kazdej krotki
#planets.sort(key=lambda x: x[n]) #sortowanie po n-tym elemencie kazdej krotki lambda jest funkcja anonimowa
planets
