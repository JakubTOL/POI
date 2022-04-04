# błąd e= l.błędnych klasygikacji/l.wszystkich wektorów
# dokładność = 1-e  miara działania klasyfikatora
# io.imshow(img_sample_grey)  # wyswietlenie dla debugowania co wyszlo
# io.show()

from skimage import io, img_as_uint  # odczyt zapis plikow, jasnosc
from skimage.color import rgb2gray  # do konwersji do skali szarosci
from skimage.feature import match_template, greycoprops, greycomatrix
import numpy as np  # do operacji na miaerzach
import pandas  # do zapisu do csv
import os  # ustawienie sciezki roboczej dla zapisu csv z pandas
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix


# funkcja podzialu dla gresu
def crop_gres(wysokosc1, wysokosc2, szerokosc1, szerokosc2):
    filepath = "D:/new/gres/gres.jpg"  # sciezka odczytu pliku bazowego
    image = io.imread(filepath)  # odczyt do zmiennej
    # oryg zdjecie 1500x1500 px
    num = 0
    # podzial dla 1 kolumny
    for i in range(0, 141):
        if wysokosc2 <= 1408:
            croppped = image[wysokosc1:wysokosc2, szerokosc1:szerokosc2]  # wymiary [od_y1:do_y2, od_x1:do_x2]
            # io.imshow(croppped)  # wyswietlenie
            # io.show()
            savepath = "D:/new/gres/gres_crop" + str(num) + ".jpg"  # zapis po sciezce z inkrementacja nazwy pliku
            io.imsave(savepath, croppped)  # zapisz img (sciezka, co_zapisac)
            num += 1
            wysokosc1 = wysokosc2
            wysokosc2 += 128
        else:
            wysokosc1 = 0
            wysokosc2 = 128
            szerokosc1 += 128
            szerokosc2 += 128


# funkcja podzialu dla celgy
def crop_cegla(wysokosc1, wysokosc2, szerokosc1, szerokosc2):
    filepath = "D:/new/cegla/cegla.jpg"  # sciezka odczytu pliku bazowego
    image = io.imread(filepath)  # odczyt do zmiennej
    num = 0
    # podzial dla 1 kolumny
    for i in range(0, 141):
        if wysokosc2 <= 1408:
            croppped = image[wysokosc1:wysokosc2, szerokosc1:szerokosc2]  # wymiary [od_y1:do_y2, od_x1:do_x2]
            savepath = "D:/new/cegla/cegla_crop" + str(num) + ".jpg"  # zapis po sciezce z inkrementacja nazwy pliku
            io.imsave(savepath, croppped)  # zapisz img (sciezka, co_zapisac)
            num += 1
            wysokosc1 = wysokosc2
            wysokosc2 += 128
        else:
            wysokosc1 = 0
            wysokosc2 = 128
            szerokosc1 += 128
            szerokosc2 += 128


# funkcja podzialu dla celgy
def crop_drewno(wysokosc1, wysokosc2, szerokosc1, szerokosc2):
    filepath = "D:/new/drewno/drewno.jpg"  # sciezka odczytu pliku bazowego 1500x1200px
    image = io.imread(filepath)  # odczyt do zmiennej
    num = 0
    # podzial dla 1 kolumny
    for i in range(0, 141):
        if wysokosc2 <= 1408:
            croppped = image[wysokosc1:wysokosc2, szerokosc1:szerokosc2]  # wymiary [od_y1:do_y2, od_x1:do_x2]
            savepath = "D:/new/drewno/drewno_crop" + str(num) + ".jpg"  # zapis po sciezce z inkrementacja nazwy pliku
            io.imsave(savepath, croppped)  # zapisz img (sciezka, co_zapisac)
            num += 1
            wysokosc1 = wysokosc2
            wysokosc2 += 128
        else:
            wysokosc1 = 0
            wysokosc2 = 128
            szerokosc1 += 128
            szerokosc2 += 128


def read_and_calc():
    # odczyt kolejnych probek wycietych ze zdejecia ref
    num = 0
    # parametry do macierzy glcm
    ang = (0, np.pi/4, np.pi/2, 3*np.pi/4)
    dist = (1, 3, 5)
    prop_name = ('dissimilarity', 'correlation', 'contrast', 'energy', 'homogeneity', 'ASM')
    cat1 = ['drewno']
    os.chdir('D:/new')  # sciezka robocza dla zapisu csv z pandas
    for i in range(1, 130):
        # odczyt wycinkow drewna
        filepath = "D:/new/drewno/drewno_crop" + str(num) + ".jpg"
        sample = io.imread(filepath)
        img_sample_grey = rgb2gray(sample)  # konwersja do skali szarosci
        img_sample_grey_conv = (img_sample_grey/np.max(img_sample_grey)*63).astype('uint8')
        glcm = greycomatrix(img_sample_grey_conv,distances=dist,angles=ang,levels=64,symmetric=True,normed=True)

        num += 1  # iteracja dla wczytania kolejnych próbek
        properties = []
        for prop in prop_name:
            properties.extend(list(greycoprops(glcm, prop).flatten()))
            properties.extend(cat1)
    frame = pandas.DataFrame(data=properties)  # formatowanie ramki danych
    frame.to_csv('properties.csv', sep=',', index=False)  # nazwa pliku, uzywany separator, indeksowanie pozycji


def klasyfikator():
    data = pandas.read_csv("D:/new/properties.csv")
    x = data.drop('category', axis=1)
    y = data['category']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
    klasyfikacja = SVC(kernel='linear')
    klasyfikacja.fit(x_train, y_train)
    y_pred = klasyfikacja.predict(x_test)
    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))


if __name__ == '__main__':
    # funkcje do odczytu zdjeciea z folderu i podzialu na mniejsze fragmenty
    crop_gres(0, 128, 0, 128)  # wywołanie funkcji z parametrami wymiarow [od_y1:do_y2, od_x1:do_x2]
    crop_cegla(0, 128, 0, 128)
    crop_drewno(0, 128, 0, 128)
    # funkcja odczytu
    read_and_calc()
    klasyfikator()
