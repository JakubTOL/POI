# import pakierów i modulow do zadania 4
import numpy as np
from keras import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# wczytanie danych pliku .csv z zad 3   pd.read_csv

# Wyodrebnienie pakietu cech do macierzy X

# wyodrebnienie etykiet gategorii do wektora y

# Kodowanie calkowitoliczbowe dla wektora y -> y_int

#kodowanie 1 z n dla wektora y_int -> y_onehot

# podzial zbioru X oraz wektora y_onehot na czesc treningowa 70% i 30% testowa
# X_train, X_test, y_train, y_test = train_test_split(X, onehot_encoded, test_size=0.3)
