import tensorflow as tf
import os
print(tf.__version__)

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

physical_devices = tf.config.list_physical_devices("GPU")
print(physical_devices)
tf.config.experimental.set_memory_growth(physical_devices[0], True)


import pandas as pd
import csv
import numpy as np

dataset_path = "shoulder.csv"

df = pd.read_csv(dataset_path)
df.head()

y = np.array(df["class"])
x = np.array(df.drop("class", axis = "columns"))
print(x)
print(y)

import collections
collections.Counter(y)

from sklearn.preprocessing import LabelEncoder,StandardScaler

encoder = LabelEncoder()
y = encoder.fit_transform(y)
y

print(x.shape)
print(x[0].shape)
print(x)

encoder.classes_

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

print(x_train.shape)
print(x_train[0].shape)

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential()
model.add(Dense(32, input_dim = x_train[0].shape[0], activation = 'relu'))
model.add(Dropout(0.1))
model.add(Dense(16, activation = 'relu'))
model.add(Dropout(0.1))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(len(encoder.classes_), activation='softmax'))

model.summary()

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs = 500, validation_data=(x_test,y_test), verbose=0)

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(history.history['accuracy'][-1])
print(history.history['val_accuracy'][-1])

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(history.history['loss'][-1])
print(history.history['val_loss'][-1])

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

larger_model = Sequential()
larger_model.add(Dense(128, input_dim = x_train[0].shape[0], activation = 'relu'))
larger_model.add(Dropout(0.1))
larger_model.add(Dense(64, activation = 'relu'))
larger_model.add(Dropout(0.1))
larger_model.add(Dense(32, activation = 'relu'))
larger_model.add(Dense(len(encoder.classes_), activation='softmax'))

larger_model.summary()
from tensorflow.keras.utils import plot_model
larger_model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history_larger = larger_model.fit(x_train, y_train, epochs = 500, validation_data=(x_test,y_test), verbose=0)

import matplotlib.pyplot as plt

plt.plot(history_larger.history['accuracy'])
plt.plot(history_larger.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(history_larger.history['accuracy'][-1])
print(history_larger.history['val_accuracy'][-1])

plt.plot(history_larger.history['loss'])
plt.plot(history_larger.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(history_larger.history['loss'][-1])
print(history_larger.history['val_loss'][-1])

model.save("models/squats_small.h5")

larger_model.save("models/squats_large.h5")

