# błąd e= l.błędnych klasygikacji/l.wszystkich wektorów
# dokładność = 1-e  miara działania klasyfikatora

from skimage import io, exposure, img_as_uint  # odczyt zapis plikow, jasnosc
from skimage.color import rgb2gray  # do konwersji do skali szarosci
from skimage.feature import match_template, greycoprops, greycomatrix
import numpy as np  # do operacji na miaerzach
import pandas  # do zapisu do csv


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


def odczyt():
    # odczyt zdjecia referencyjnego i jego obroka
    filepath_ref = "D:/new/drewno/drewno.jpg"
    ref_img = io.imread(filepath_ref)
    ref_grey = rgb2gray(ref_img)
    ref_brightness = exposure.adjust_gamma(ref_grey, gamma=5, gain=1)

    # odczyt kolejnych probek wycietych ze zdejecia ref
    num = 0
    properies = []
    samples_all = []
    samples_drewno = []
    samples_cegla = []
    samples_gres = []
    category = ["drewno", "cegla", "gres"]
    dissimilarity = []
    correlation = []
    for i in range(0, 130):
        # odczyt wycinkow drewna
        filepath = "D:/new/drewno/drewno_crop" + str(num) + ".jpg"
        sample = io.imread(filepath)
        img_sample_grey = rgb2gray(sample)  # konwersja do skali szarosci
        img_sample_grey = exposure.rescale_intensity(img_sample_grey, in_range=(5, 64))  # głebia jasnosci do 64 poziomu
        # io.imshow(img_brightness)  # wyswietlenie dla debugowania co wyszlo
        # io.show()
        samples_drewno = img_as_uint(img_sample_grey)
        # odczyt wycinkow cegly
        filepath = "D:/new/cegla/cegla_crop" + str(num) + ".jpg"
        sample = io.imread(filepath)
        img_sample_grey = rgb2gray(sample)  # konwersja do skali szarosci
        img_sample_grey = exposure.rescale_intensity(img_sample_grey, in_range=(5, 64))
        samples_cegla = img_as_uint(img_sample_grey)
        # odczyt wycinkow gresu
        filepath = "D:/new/gres/gres_crop" + str(num) + ".jpg"
        sample = io.imread(filepath)
        img_sample_grey = rgb2gray(sample)  # konwersja do skali szarosci
        img_sample_grey = exposure.rescale_intensity(img_sample_grey, in_range=(5, 64))
        samples_gres = img_as_uint(img_sample_grey)

        samples_all = samples_drewno + samples_cegla + samples_gres  # zlaczenie wszystkich probek roznych kategorii
        # okreslic dissimilarity, correlation, constrast, energy, homogenity, ASM ]
        # odleglosci pikseli 1, 3, 5                                              ] to z macierzy glcm
        # 4 kierunki 0, 45, 90, 135 stopni                                        ]
        glcm = greycomatrix(samples_all,distances=[1,3,5],angles=[0,45,90,135],levels=64,symmetric=True,normed=True)
        dissimilarity.append(greycoprops(glcm, 'dissimilarity')[0, 0])
        correlation.append(greycoprops(glcm, 'correlation')[0, 0])
        num += 1
    print(glcm)


if __name__ == '__main__':
    # funkcje do odczzytu zdjeciea z folderu i podzialu na mniejsze fragmenty
    # crop_gres(0, 128, 0, 128)  # wywołanie funkcji z parametrami wymiarow [od_y1:do_y2, od_x1:do_x2]
    # crop_cegla(0, 128, 0, 128)
    # crop_drewno(0, 128, 0, 128)
    # funkcja odczytu
    odczyt()
