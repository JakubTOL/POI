from csv import writer
import numpy as np


def generate_points():  # definicja fukcji z parametrem domyslnym
    #definiowanie obiektow z parametrami rozkladu normalnego
    us = np.linspace(0, 2 * np.pi, 32)
    zs = np.linspace(0, 10, 2)
    us, zs = np.meshgrid(us, zs)
    xs = 10 * np.cos(us)
    ys = 10 * np.sin(us)
    #zapis punktow do pliku .csv, ale z roszerzeniem .xyz
    points = zip(xs, ys, zs)  # struktura zawierająca wygenerwoane koorydnaty ale 'zip' stworzył krotki wspolrzednych
    return points


with open('cylinder.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
    csvwriter = writer(csvfile)
    p = generate_points()
    csvwriter.writerow(p)