import tensorflow as tf
import numpy as np

x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# keras is a library that works on tensorflow
# sequential is default model 
tf.model = tf.keras.Sequential()

# uints == output shape, input_dim == input shape
# 'dense' is densely-connected NN layer.
# 
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=1))
# SGD = standard gradient descendent, lr = learning rate   
sgd = tf.keras.optimizers.SGD(lr = 0.1)                     
tf.model.compile(loss='mse', optimizer=sgd)

# prints summary of the model to the terminal
tf.model.summary()

tf.model.fit(x_train, y_train, epochs = 200)
y_predict = tf.model.predict(np.array([5, 4]))
print(y_predict)
