# import pakierów i modulow do zadania 4
import numpy as np
#  pakiet wymaga grafiki wiec uruchomić na google
#  oprocz zainstalowania wymuszenie konkretnej wersji za pomoca "!pip install tensorflow --ignore-installed --user"
#from keras import Sequential
#from keras.layers import Dense
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# wczytanie danych pliku .csv z zad 3   pd.read_csv
# Wyodrebnienie pakietu cech do macierzy X
filepath = "D:/new/properties.csv"
X = pd.read_csv(filepath, sep=',')
#print(X)
# wyodrebnienie etykiet gategorii do wektora y
X_conv = np.array(X)  # konwesja X do macierzy pakitu np
print(X_conv)
y = X_conv[:,12]  # odczytanie do zmiennej y 12 kolumny macierzy X_conv
print(y)
# Kodowanie calkowitoliczbowe dla wektora y -> y_int
#y_int = int(np.transpose(y))
#print(y_int)
#kodowanie 1 z n dla wektora y_int -> y_onehot

# podzial zbioru X oraz wektora y_onehot na czesc treningowa 70% i 30% testowa
# X_train, X_test, y_train, y_test = train_test_split(X, onehot_encoded, test_size=0.3)
