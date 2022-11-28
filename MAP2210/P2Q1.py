from scipy.sparse import linalg as linalg_sparse
from scipy.sparse import lil_matrix
from scipy import linalg
from math import cos,sin,exp,pi,log
import numpy as np
import math 
import matplotlib.pyplot as plt
from time import time

def fx(f,x0,x1,n):
    return np.array([f(x0 + (x1-x0)/n * i) for i in range(1,n)])

def P2Q1(f0, f1, x0, x1, n, b):
    """
    Consideraremos b dado e logo a(x) = h²*b(x)
    Consideraremos (3) para a primeira componente
    Consideraremos (5) para a demais componentes
    Consideraremos (2) para a ultima componente
    ex: | 2   -5   4  -1    0   0 | |u1|  |-a|
        | 16 -30  16  -1    0   0 | |u2|  |-12a + u0 |
        | -1  16 -30  16   -1   0 | |u3|  |-12a|
        | 0   -1  16 -30   16  -1 | |u4|  |-12a|
        | 0    0  -1  16  -30  16 | |u5|  |-12a + u7 |
        | 0    0   0   0    1  -2 | |u6|  |-a -u7|
    """
    t = time()
    a = b*((x1-x0)/n)**2
    if(n>=5):
        #A = np.array([[0]*(n-1)]*(n-1))
        A = lil_matrix((n-1,n-1))
        #print(A)
        for i in range(n-1):
            if(i==0):
                A[i,i] = 2
                A[i,i+1] = -5
                A[i,i+2] = 4
                A[i,i+3] = -1
                a[i] = -a[i]
            elif(i==n-2):
                A[i,i] = -2
                A[i,i-1] = 1
                a[i] = -a[i] - f1
            else:
                a[i] = -12*a[i]
                if(i>1):
                    A[i,i-2] = -1
                else:
                    a[i] = a[i] + f0
                A[i,i-1]=16
                A[i,i]=-30
                A[i,i+1]=16
                #print(i,n-2,i+2)
                if(i<n-3):
                    A[i,i+2]=-1
                else:
                    a[i] = a[i] + f1
    else:
        print("numero de colunas insuficientes")
    A = A.tocsr()
    return linalg_sparse.spsolve(A,a),A,time()-t
    #return linalg.solve(A,a),A,time()-t

n=64
x0 = 0
x1 = 2*pi
#x1 = 1
#f0 = 0
f0 = exp(1)
f1 = exp(1)
#f1 = 3
#

erro = np.array([0.]*10)
erroinf = np.array([0.]*10)
for j in range(1,10):
    n = n*2
    f = lambda x:(cos(x)-sin(x)**2)*exp(cos(x))
    #f = lambda x:-5
    b = fx(f,x0,x1,n)
    aprox,A,t = P2Q1(f0, f1, x0, x1, n, b)
    g = lambda x:exp(cos(x))
    #g = lambda x:x/2 + (5*x**2)/2
    gx = fx(g,x0,x1,n)
    erro[j] = 0
    erroinf[j] = 0
    err2 = np.array([0.]*(n-1))
    for i in range(n-1):
        err2[i] = (gx[i]-aprox[i])**2
        erroinf[j] = abs(gx[i]-aprox[i]) if abs(gx[i]-aprox[i])>erroinf[j] else erroinf[j] 
        erro[j] = erro[j] + err2[i]
    erro[j] = erro[j]**(1/2)
    print("{} & {:.5e} & {:.5e}\\\\".
          format(n,
          (x1-x0)/n,
          t))
    fig, axs = plt.subplots(2, 2,constrained_layout=True)
    axs[0,0].plot(b)
    axs[0,0].set_title("u''")
    axs[0,1].plot(gx)
    axs[0,1].set_title("u")
    axs[1,0].plot(aprox)
    axs[1,0].set_title("aprox")
    axs[1,1].set_title("(erro norma2)²")
    axs[1,1].plot(err2)
    title = 'n = '+ str(n)
    fig.suptitle(title)
    plt.show()

#m = [[1 1 1 2],[2 2 4 8],[0 0 1 2]] 
#a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
#b = np.array([2, 4, -1])
#x = linalg.solve(a, b)
#print(x)
