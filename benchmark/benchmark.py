import numpy as np
import time 
import matplotlib.pyplot as plt
from LinearProblem import LinearProblem

def generateDataset(dim):
    m,n = dim[0],dim[1]
    A = np.random.rand(m,n)
    b = np.random.rand(m)
    c = np.random.rand(n)
    return A,b,c

sizes = [[2000,3000],[10000,15000],[20000,30000]]
nparam = []
t_elapsed = []
for s in sizes:
    A,b,c = generateDataset(s)
    begin = time.time()
    prob = LinearProblem(A,b,c)
    sol = prob.solve("simplex")
    end = time.time()
    delta = 1000*(end-begin) #milliseconds
    t_elapsed.append(delta)
    nparam.append(s[0]*s[1])

plt.plot(nparam,t_elapsed)
plt.grid(True)
plt.title("Performance Test")
plt.xlabel("Number of Parameters (n*m)")
plt.ylabel("Execution time [ms]")
plt.show()