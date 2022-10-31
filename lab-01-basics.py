'''
tensorflow1 hello world examples

import tensorflow as tf

hello = tf.constant("Hello, Tensorflow!")
session = tf.Session()
print(session.run(hello))
''' 


# tensorflow2 support eager execution for default. (not, graph exeuction)
# so, there is no session and graph in TF2. 
# Eager Execution -vs- Graph Execution : https://towardsdatascience.com/eager-execution-vs-graph-execution-which-is-better-38162ea4dbf6 

import tensorflow as tf

msg = tf.constant("Tensorflow 2.0 Hello Wolrd!")
tf.print(msg) 