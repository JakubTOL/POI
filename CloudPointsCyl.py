from csv import writer
import numpy as np
import random

theta = np.linspace(0, 2 * np.pi, 2000)
promien = 20
x = promien * np.cos(theta)
x = x.reshape(2000, 1)
y = promien * np.sin(theta)
y = y.reshape(2000, 1)
lista_wysokosci = []
for i in range(0, 2000):
    n = random.randint(1, 2000)
    lista_wysokosci.append(n)
z = np.array(lista_wysokosci)
z = z.reshape(2000, 1)
wynik = np.concatenate((x, y, z), axis=1)


with open('CloudPointsCyl.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
    csvwriter = writer(csvfile)
    for p in wynik:  # iteracja po pakietach punktow 'zip'
        csvwriter.writerow(p)  # zapisz do pliku konkretna krotke
