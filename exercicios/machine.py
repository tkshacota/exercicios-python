import tensorflow as tf
from tensorflow import Operation
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.framework.ops import _EagerTensorBase

x_train = tf.constant([[1.0], [2.0], [3.0], [4.0],])
y_train = tf.constant([[2.0], [4.0], [6.0], [8.0],])

model = Sequential()
model.add(Dense(units=1, input_shape=(1,)))
model.compile(optimizer='sgd', loss='mean_squared_error')
history = model.fit(x_train, y_train, epochs=1000, verbose=0)

x_new = tf.constant([[5.0]])
prediction = model.predict(x_new, verbose=0)
print(f"predicao para x=5: {prediction[0][0]:.2f} (esperado: 10)")