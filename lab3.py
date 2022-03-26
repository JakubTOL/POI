# błąd e= l.błędnych klasygikacji/l.wszystkich wektorów
# dokładność = 1-e  miara działania klasyfikatora

from skimage import io


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
    for i in range(0, 110):
        if wysokosc2 <= 1152:
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


if __name__ == '__main__':
    # funkcje do odczzytu zdjeciea z folderu i podzialu na mniejsze fragmenty
    crop_gres(0, 128, 0, 128)  # wywołanie funkcji z parametrami wymiarow [od_y1:do_y2, od_x1:do_x2]
    crop_cegla(0, 128, 0, 128)
    crop_drewno(0, 128, 0, 128)
    #