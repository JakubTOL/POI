# import pakierów i modulow do zadania 4
import numpy as np
#  pakiet wymaga grafiki wiec uruchomić na google
#  oprocz zainstalowania wymuszenie konkretnej wersji za pomoca "!pip install tensorflow --ignore-installed --user"
from keras import Sequential
from keras.layers import Dense
import pandas as pd
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# wczytanie danych pliku .csv z zad 3   pd.read_csv
filepath = "D:/new/properties.csv"
df = pd.read_csv(filepath, sep=',')
data = df.to_numpy()
# Wyodrebnienie pakietu cech do macierzy X
X = data[:,:-1].astype('float')
y = data[:,-1]

label_encoder = LabelEncoder()
int_encoder = label_encoder.fit_transform(y)

onehot_encoder = OneHotEncoder(sparse=False)
int_encoder = int_encoder.reshape(len(int_encoder),1)
onehot_encoder = onehot_encoder.fit_transform((int_encoder))

X_train, X_test, y_train, y_test = train_test_split(X, onehot_encoder, test_size=0.3)

model = Sequential()
model.add(Dense(10, input_dim=72, activation='sigmoid'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.summary()
model.fit(X_train, y_train, epochs=100, batch_size=10, shuffle=True)

y_pred = model.predict(X_test)
y_pred_int = np.argmax(y_pred, axis=1)
y_test_int = np.argmax(y_test, axis=1)
conf_mat = confusion_matrix(y_test_int, y_pred_int)
print(conf_mat)
