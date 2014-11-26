#algoritmo de ED

from numpy import *
import matplotlib.pyplot as plt

def evaluate(x):
    return (x*x).sum(axis=1)

def rand(lim):
    vec = zeros((lim))
    for i in range (lim):
        vec[i]=i
    random.shuffle(vec)
    return vec[:3]

nv=0

CR = .5
F = 1
lS = 10
lI = -10

dims = 2
parts = 5

gmax=30

x = random.random((parts,dims))
x = x*(lS-lI)+lI
u=zeros((parts,dims))
fx_best = []
while nv<gmax:
    for i in range(len(x)):
        vec = rand(len(x))
        r1 = vec[0]
        r2 = vec[1]
        r3 = vec[2]
        jr = random.randint(0,dims)
        for j in range(dims):
            if random.random() < CR or j==jr:
                u[i] = x[r3][j] + F * (x[r1][j]-x[r2][j])
            else:
                u = x.copy()
        fx=evaluate(x)
        fu=evaluate(u)
        if fu[i] <= fx[i]:
            x[i] = u[i].copy()
        else:
            x[i]=x[i].copy()
    fx_best.append(fx)
    nv+=1
print(fx)

for z in range (len(fx_best)):
    print(fx_best[z])
