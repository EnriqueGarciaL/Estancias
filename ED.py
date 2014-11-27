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

def escribir(fx):
    file = open("datos.txt","a+")
    for x in range(len(fx)):
        file.write(str(fx[x])+"\t")
    file.write("\n")
    file.close()

def ejecute(lS,lI,fun):
    nv=0
    CR = .5
    F = .9
    dims = 2
    parts = 5
    gmax=30

    x = random.random((parts,dims))
    x = x*(lS-lI)+lI
    u=zeros((parts,dims))

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
            fx=fun(x)
            fu=fun(u)
            if fu[i] <= fx[i]:
                x[i] = u[i].copy()
            else:
                x[i]=x[i].copy()
        nv+=1
    escribir(fx)

def main():
    ejecute(10,-10,evaluate)

main()
