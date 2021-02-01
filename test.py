import numpy as np
from scipy.stats import truncnorm
import matplotlib.pyplot as plt


from scipy.stats import skewnorm
a=0.2
data= skewnorm.rvs(a, size=100)
a = np.array(data)
a = np.sort(a)
print(a)
print(np.mean(a),np.std(a))

'''
fig,ax = plt.subplots(1,1)
a, b = (0 - 0.1) / 1, (1 - 0.1) / 1
r = truncnorm.rvs(a, b, size = 100)
a = np.array(r)
print(a)
print(np.std(a))
'''
