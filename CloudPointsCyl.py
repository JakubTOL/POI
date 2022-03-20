from csv import writer
import random
import numpy as np

promien = 5
theta = random.random() * 2 * np.pi
x = promien * np.cos(theta)
y = promien * np.sin(theta)
for z in range(0, 2000):
    z += 1
points = zip(x, y, z)  # struktura zawierająca wygenerwoane koorydnaty ale 'zip' stworzył krotki wspolrzednych


if __name__ == '__main__':  # aby importowac tylko procedure generate_points
    with open('CloudPoints.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        csvwriter.writerow(p)
