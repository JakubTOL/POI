from scipy.stats import norm  # import pakietu rozkładu normalnego
from csv import writer
import random
import numpy


def generate_points(num_points: int = 2000):  # definicja fukcji z parametrem domyslnym
    #definiowanie obiektow z parametrami rozkladu normalnego
    distribution_x = norm(loc=0, scale=20)
    distribution_y = norm(loc=0, scale=200)
    distribution_z = norm(loc=0.2, scale=0.05)

    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)

    #zapis punktow do pliku .csv, ale z roszerzeniem .xyz
    points = zip(x, y, z)  # struktura zawierająca wygenerwoane koorydnaty ale 'zip' stworzył krotki wspolrzednych
    return points


if __name__ == '__main__':  # aby importowac tylko procedure generate_points
    cloud_points = generate_points(2000)
    with open('CloudPoints.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in cloud_points:  # iteracja po pakietach punktow 'zip'
            csvwriter.writerow(p)  # zapisz do pliku konkretna krotke
