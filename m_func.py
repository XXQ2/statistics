#coding: UTF-8
import numpy as np
import scipy as sp

test_data = np.array([1,3,3,5,5,5,7,7,9])

#平均値
ave = np.mean(test_data)

print("平均値: {}".format(ave))


#標本分散
N = len(test_data)
mu = np.sum(test_data) / N
sd = np.sum((test_data - mu) ** 2) / N

print("標本分散: {}".format(sd))


#不偏分散
ud = np.sum((test_data - mu) ** 2) / (N - 1)

print("不偏分散: {}".format(ud))


#中央値
md = sp.median(test_data)

print("中央値: {}".format(md))
