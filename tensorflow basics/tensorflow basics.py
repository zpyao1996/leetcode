import tensorflow as tf
from numpy.random import RandomState
batch_size=10
w1=tf.get_variable(name="var_1", initializer=tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.get_variable(name="var_2", initializer=tf.random_normal([3,1],stddev=1,seed=1))
# None 可以根据batch 大小确定维度，在shape的一个维度上使用None
x=tf.placeholder(tf.float32,shape=(None,2))
y=tf.placeholder(tf.float32,shape=(None,1))
# #激活函数使用ReLU
# a=tf.nn.relu(tf.matmul(x,w1))
# yhat=tf.nn.relu(tf.matmul(a,w2))
# #定义交叉熵为损失函数，训练过程使用Adam算法最小化交叉熵
# cross_entropy=-tf.reduce_mean(y*tf.log(tf.clip_by_value(yhat,1e-10,1.0)))
# train_step=tf.train.AdamOptimizer(0.001).minimize(cross_entropy)
# rdm=RandomState(1)
# data_size=516
# #生成两个特征，共data_size个样本
# X=rdm.rand(data_size,2)
# #定义规则给出样本标签，所有x1+x2<1的样本认为是正样本，其他为负样本。Y，1为正样本
# Y = [[int(x1+x2 < 1)] for (x1, x2) in X]

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(w1))
    print(sess.run(w2))
    # steps=11000
    # for i in range(steps):
    #     #选定每一个批量读取的首尾位置，确保在1个epoch内采样训练
    #     start = i * batch_size % data_size
    #     end = min(start + batch_size,data_size)
    #     sess.run(train_step,feed_dict={x:X[start:end],y:Y[start:end]})
    #     if i % 1000 == 0:
    #         training_loss= sess.run(cross_entropy,feed_dict={x:X,y:Y})
    #         print("在迭代 %d 次后，训练损失为 %g"%(i,training_loss))