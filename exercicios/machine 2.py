import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

x_unsopervised = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])

input_layer = Input(shape=(2,))
encoded = Dense (units=1)(input_layer)
decoded = Dense (units=2)(encoded)
autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mse')
autoencoder.fit(x_unsopervised, x_unsopervised,epochs=1000,verbose=0)
prediction = autoencoder.predict(x_unsopervised, verbose=0)
print("original: ", x_unsopervised.numpy())
print("reconstruido:\n", prediction)