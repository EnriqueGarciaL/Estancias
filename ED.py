#algoritmo de ED

from numpy import *
import matplotlib.pyplot as plt

def evaluate(x):
    return (x*x).sum(axis=1)

def evaluate2(x):
    return abs(x).sum(axis=1)+abs(x).prod(axis=1)

def evaluate3(x):
    suma = zeros(len(x))
    for i in range(len(x)):
        aux=0
        for j in range (len(x[i])):
            for k in range (j+1):
                aux += x[i][k]
            suma[i]+=(aux*aux).sum(axis=0)
    return suma

def rand(lim):
    vec = zeros((lim))
    for i in range (lim):
        vec[i]=i
    random.shuffle(vec)
    return vec[:3]

def escribir(fx):
    file = open("datos.txt","a+")
    for x in range(len(fx)):
        file.write(str(fx[x])+"\t")
    file.write("\n")
    file.close()

def ejecute(lS,lI,fun):
    nv= 0
    CR = 0.5
    F = 0.5
    dims = 30
    parts = 10
    gmax=2000

    x = random.random((parts,dims))
    x = x*(lS-lI)+lI
    u=zeros((parts,dims))

    while nv<gmax:
        for i in range(len(x)):
            vec = rand(len(x))
            r1 = vec[0]
            r2 = vec[1]
            r3 = vec[2]
            jr = random.randint(dims)
            for j in range(dims):
                if random.random() < CR or j==jr:
                    u[i][j] = x[r3][j] + F * (x[r1][j]-x[r2][j])
                else:
                    u[i][j] = x[i][j]
            fx=fun(x)
            fu=fun(u)
            if fu[i] <= fx[i]:
                x[i] = u[i]
            else:
                x[i]=x[i]
        nv+=1
    # escribir(fx)
    for x in range(len(fx)):
        print(str(fx[x]))

def main():
    ejecute(100,-100,evaluate3)

main()
