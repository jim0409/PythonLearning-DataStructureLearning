### Optimizer:
tf.train.GradientDescentOptimizer

tf.train.AdadeltaOptimizer

tf.train.AdagradOptimizer

tf.train.AdagradDAOptimizer

tf.train.MomentumOptimizer

tf.train.AdamOptimizer

tf.train.FtrlOptimizer

tf.train.ProximalGradientDescentOptimizer

tf.train.ProximalAdagradOptimizer

tf.train.RMSPropOptimizer

標準梯度下降法：
標準梯度下降先計算所有樣本匯總誤差，然後根據總誤差來更新權值

隨機梯度下降法：
隨機梯度下降隨機抽取一個樣本來計算誤差，然後更新權值

批量梯度下降法：
批量梯度下降算是一種折衷的方案，從傯樣本中選取一個批次（比如共有10000個樣本，隨機選取100個樣本作為一個batch)，
然後計算這個batch的總誤差，根據總誤差來更新權值。


