import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


arr = np.loadtxt("data/double1-s1s1.csv", delimiter=",", dtype='int16')

means = []

for i in range(10):
    temp = []
    for j in range(10000):
        temp.append(1-np.mean(arr[10000 * i: 10000 * i + j + 1]))
    means.append(temp)

means = np.array(means)
means = np.transpose(means)

plt.figure(figsize=(9, 6), dpi=100)
_ = plt.plot([i for i in range(10000)],means, color='k')


plt.xlabel("Number of games")
plt.ylabel("Expectation Game Length")
# plt.title("Expectation of Single Player with Strategy " + str(num) + " of 10 runs of 1000 simulations")

plt.show()
