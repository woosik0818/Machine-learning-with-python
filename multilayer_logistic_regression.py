import numpy as np
import tensorflow as tf

inp = np.loadtxt('learning_data_trans.txt', delimiter=',', dtype=np.float32)
inp2 = np.loadtxt('test_data_trans.txt', delimiter=',', dtype=np.float32)

learning_rate = 0.01
training_iter = 10000

input_data_learning = inp[:, 0:-1]
input_data2_learning = inp[:,[-1]]
input_data_test = inp2[:, 0:-1]
input_data2_test = inp2[:,[-1]]
print("learningx:", input_data_learning)
print("learningy:", input_data2_learning)
print("testx:", input_data_test)
print("testy:", input_data2_test)

x = tf.placeholder(tf.float32, shape=[None, 12])
y = tf.placeholder(tf.float32, shape=[None, 1])

w1 = tf.get_variable("w1", shape=[12, 12], initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([12]))
L1 = tf.sigmoid(tf.matmul(x, w1) + b1)

w2 = tf.get_variable("w2", shape=[12, 12], initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([12]))
L2 = tf.sigmoid(tf.matmul(L1, w2) + b2)

w3 = tf.get_variable("w3", shape=[12, 1], initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([1]))

#hypothesis = tf.nn.softmax(tf.matmul(L2, w3) + b3)
#cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(hypothesis), axis=1))
hypothesis = tf.sigmoid(tf.matmul(L2, w3) + b3)
cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1 - y) * tf.log(1 - hypothesis))

train = tf.train.GradientDescentOptimizer(learning_rate = learning_rate).minimize(cost)
init = tf.initialize_all_variables()
"""
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.float32))
"""
with tf.Session() as sess:
	sess.run(init)
	
	feed = {x: input_data_learning, y: input_data2_learning}

	for step in range(training_iter):
		sess.run(train, feed_dict=feed)
		if step % 200 == 0:
			print (step, sess.run(cost, feed_dict={x: input_data_learning, y: input_data2_learning}))
	predicted = tf.equal(tf.floor(hypothesis+0.5), y)
	accuracy = tf.reduce_mean(tf.cast(predicted, "float32"))
	print (sess.run([hypothesis, tf.floor(hypothesis+0.5), predicted, accuracy], feed_dict={x: input_data_test, y: input_data2_test}))
	print ("Accuracy:", accuracy.eval({x: input_data_test, y: input_data2_test}))

