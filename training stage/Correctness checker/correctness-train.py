# %%
import os
import random
import pandas as pd
import numpy as np
import tensorflow as tf


# %%
dataset=[]
y=[]
Fs = 10
root_path = "squats/"

classes = os.listdir(root_path)
print(classes)
for class_name in classes:
    class_path = root_path + "/" + class_name
    files = [class_path + "/" + f for f in os.listdir(class_path) if os.path.isfile(class_path + '/' + f)]
    for file in files:
      df = pd.read_csv(file)
      df = df.iloc[:,36:]
      if root_path == "squats/":
        for i in range(14, 24, 1):
          df=df.drop("x"+str(i), axis = "columns")
          df=df.drop("y"+str(i), axis = "columns")
          df=df.drop("z"+str(i), axis = "columns")
          df=df.drop("v"+str(i), axis = "columns")
      for i in range(len(df) - Fs):
          dataset.append(df.iloc[i:i+Fs].to_numpy())
          y.append(class_name)


# %%
len(y)


# %%
unique, counts = np.unique(np.array(y), return_counts=True)
dict(zip(unique, counts))


# %%
y = np.array(y)
dataset = np.asarray(dataset)


# %%
dataset.shape


# %%
from sklearn.preprocessing import LabelEncoder,StandardScaler

encoder = LabelEncoder()
y = encoder.fit_transform(y)
y = tf.keras.utils.to_categorical(y)
y


# %%
encoder.classes_


# %%
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(dataset, y, test_size=0.33, random_state=42)


# %%
print(x_train.shape)
print(x_test.shape)
print(x_train[0].shape)


# %%
from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, TimeDistributed, LSTM, Input, Dropout
from keras.layers.convolutional import Conv1D, MaxPooling1D

cnn = Sequential()
cnn.add(Conv1D(filters=32, kernel_size=2, activation='relu', input_shape=(x_train[0].shape)))
cnn.add(MaxPooling1D(pool_size=2))
cnn.add(Flatten())
cnn.add(Dense(len(classes),activation="softmax"))
cnn.summary()
cnn.compile(optimizer = "adam", loss="categorical_crossentropy", metrics = ['accuracy'])
cnn_hist = cnn.fit(x_train, y_train, epochs = 100, validation_data = (x_test, y_test), verbose = 1, batch_size=32)


# %%
import matplotlib.pyplot as plt

plt.plot(cnn_hist.history['accuracy'])
plt.plot(cnn_hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(cnn_hist.history['accuracy'][-1])
print(cnn_hist.history['val_accuracy'][-1])


# %%
import matplotlib.pyplot as plt

plt.plot(cnn_hist.history['loss'])
plt.plot(cnn_hist.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(cnn_hist.history['loss'][-1])
print(cnn_hist.history['val_loss'][-1])


# %%
from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, TimeDistributed, LSTM, Input, Dropout
from keras.layers.convolutional import Conv1D, MaxPooling1D

cnn_large = Sequential()
cnn_large.add(Conv1D(filters=512, kernel_size=2, activation='relu', input_shape=(x_train[0].shape)))
cnn_large.add(MaxPooling1D(pool_size=2))
cnn_large.add(Dense(256))
cnn_large.add(Conv1D(filters=128, kernel_size=2, activation='relu', input_shape=(x_train[0].shape)))
cnn_large.add(MaxPooling1D(pool_size=2))
cnn_large.add(Flatten())
cnn_large.add(Dense(len(classes),activation="softmax"))
cnn_large.summary()
cnn_large.compile(optimizer = "adam", loss="categorical_crossentropy", metrics = ['accuracy'])

import time

start = time.time()

cnn_large_hist = cnn_large.fit(x_train, y_train, epochs = 100, validation_data = (x_test, y_test), verbose = 1, batch_size=32)

end = time.time()
print(end - start)


# %%
import matplotlib.pyplot as plt

plt.plot(cnn_large_hist.history['accuracy'])
plt.plot(cnn_large_hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(cnn_large_hist.history['accuracy'][-1])
print(cnn_large_hist.history['val_accuracy'][-1])


# %%
import matplotlib.pyplot as plt

plt.plot(cnn_large_hist.history['loss'])
plt.plot(cnn_large_hist.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(cnn_large_hist.history['loss'][-1])
print(cnn_large_hist.history['val_loss'][-1])


# %%
from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, TimeDistributed, LSTM, Input, Dropout
from keras import optimizers


lstm_short = Sequential()

lstm_short.add(LSTM(units = 32, activation = "tanh", input_shape = (x_train[0].shape)))

lstm_short.add(Dense(len(classes), activation = 'softmax'))

lstm_short.summary()

optimizer = optimizers.Adam(clipvalue=1)

lstm_short.compile(optimizer = optimizer, loss="categorical_crossentropy", metrics = ['accuracy'])

import time

start = time.time()

lstm_short_hist = lstm_short.fit(x_train, y_train, epochs = 50, validation_data = (x_test, y_test), verbose = 1, batch_size=32)

end = time.time()
print(end - start)


# %%
from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, TimeDistributed, LSTM, Input, Dropout

lstm_long = Sequential()

lstm_long.add(LSTM(units = 64, activation = "tanh", return_sequences = True, input_shape = (x_train[0].shape)))

lstm_long.add(Dropout(0.1))

lstm_long.add(LSTM(units= 32, activation = "tanh"))

lstm_long.add(Dense(len(classes), activation = 'softmax'))

lstm_long.summary()

lstm_long.compile(optimizer = "adam", loss="categorical_crossentropy", metrics = ['accuracy'])

import time

start = time.time()

lstm_long_hist = lstm_long.fit(x_train, y_train, epochs = 50, validation_data = (x_test, y_test), verbose = 1, batch_size=32)

end = time.time()
print(end - start)


# %%
from keras.layers import Input, Dense, LSTM, MaxPooling1D, Conv1D, TimeDistributed
from keras.models import Model

input_layer = Input(shape=(x_train[0].shape))
conv1 = Conv1D(filters=32,
               kernel_size=8,
               strides=1,
               activation='relu')(input_layer)
pool1 = MaxPooling1D(pool_size=2)(conv1)
lstm1 = LSTM(32)(pool1)
output_layer = Dense(len(classes), activation='softmax')(lstm1)
cnn_lstm = Model(inputs=input_layer, outputs=output_layer)
cnn_lstm.summary()

cnn_lstm.compile(optimizer = "adam", loss="categorical_crossentropy", metrics = ['accuracy'])

import time

start = time.time()

cnn_lstm_hist = cnn_lstm.fit(x_train, y_train, epochs = 100, validation_data = (x_test, y_test), verbose = 1, batch_size=32)

end = time.time()
print(end - start)


# %%
import matplotlib.pyplot as plt

plt.plot(cnn_lstm_hist.history['accuracy'])
plt.plot(cnn_lstm_hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(cnn_lstm_hist.history['accuracy'][-1])
print(cnn_lstm_hist.history['val_accuracy'][-1])


# %%
import matplotlib.pyplot as plt

plt.plot(cnn_lstm_hist.history['loss'])
plt.plot(cnn_lstm_hist.history['val_loss'])
plt.title('model accuracy')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(cnn_lstm_hist.history['loss'][-1])
print(cnn_lstm_hist.history['val_loss'][-1])


# %%
import matplotlib.pyplot as plt

plt.plot(lstm_long_hist.history['accuracy'])
plt.plot(lstm_long_hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(lstm_long_hist.history['accuracy'][-1])
print(lstm_long_hist.history['val_accuracy'][-1])


# %%
import matplotlib.pyplot as plt

plt.plot(lstm_long_hist.history['loss'])
plt.plot(lstm_long_hist.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(lstm_long_hist.history['loss'][-1])
print(lstm_long_hist.history['val_loss'][-1])


# %%
import matplotlib.pyplot as plt

plt.plot(lstm_short_hist.history['accuracy'])
plt.plot(lstm_short_hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(lstm_short_hist.history['accuracy'][-1])
print(lstm_short_hist.history['val_accuracy'][-1])


# %%
import matplotlib.pyplot as plt

plt.plot(lstm_short_hist.history['loss'])
plt.plot(lstm_short_hist.history['val_loss'])
plt.title('model accuracy')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
print(lstm_short_hist.history['loss'][-1])
print(lstm_short_hist.history['val_loss'][-1])


# %%
cnn.save("models/squat/squat_cnn_short.h5")


# %%
cnn_large.save("models/squat/squat_cnn_large.h5")


# %%
lstm_short.save("models/squat/squat_lstm_short.h5")


# %%
lstm_long.save("models/squat/squat_lstm_long.h5")


# %%
cnn_lstm.save("models/squat/squat_cnn_lstm.h5")


# %%
samples = x_train[:100]

import datetime

new_samples=[]
for s in samples:
    new_samples.append(s.reshape(1,10,56))

start_time = datetime.datetime.now()

for sample in new_samples:
    lstm_long.predict(sample)

end_time = datetime.datetime.now()

time_diff = (end_time - start_time)


print(time_diff.total_seconds() * 1000 / 100)
print(start)


