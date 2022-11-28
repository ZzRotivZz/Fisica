#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
#Escreva seu nome e numero USP
INFO = {9379548:"Vitor Gonçalves Ribeiro"}
A = 0.45059184  # A = 0.rg
B = 0.37324460852  # B = 0.cpf
Erro = 0.0005
# wolfram 0.788536


def f(x):
    """
    Esta funcao deve receber x e devolver f(x), como especifcado no enunciado
    Escreva o seu codigo nas proximas linhas
    """
    
    return math.exp(-A*x)*math.cos(B*x)
    #return -A*math.exp(-A*x)*math.cos(B*x) - math.exp(-A*x)*math.sin(B*x)    





def crude(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo crude
    Escreva o seu codigo nas proximas linhas
    """
    #Estimação Inicial de n
    n = 40
    r = 0
    total = 0
    m = []
    while(total<n):
        for i in range(40):
            x = random.random()
            r += f(x)
            total += 1
            m.append(r/total)
        E = Erro * r/total
        n = int((1.960**2 * np.std(m)**2) / E**2)
        #print(total,n,E,r/total,np.mean(m),np.std(m))
    plt.plot(m)
    print("Total ",total, "n ",n)

    return r/total





def hit_or_miss(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo hit or miss
    Escreva o seu codigo nas proximas linhas
    """
    E = Erro * 1/2
    sigma = 1/2**2
    n = (1.960**2 * sigma) / E**2
    # n Inicial = 1.536.640.000
    
    total = 0
    certos = 0
        
    while(total<n):
        r = int(n*(0.05/100))
        #faz o passo por uma proporção do n
        for j in range(r): 
            for i in range(100):
                x = random.random()
                y = random.random()
                certos += 1 if y<f(x) else 0
                total += 1

        perc = certos/total
        
        E = Erro * perc

        sigma = (perc)*(1-perc)
        n = (1.960**2 * sigma) / E**2
    print('Total ',total,' n ',n)
    return perc



    #return #Retorne sua estimativa







def control_variate(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo control variate
    Escreva o seu codigo nas proximas linhas
    """
    #Estimação Inicial de n
    n = 40
    r = 0
    a = 1
    b = 3
    total = 0
    m = []
    while(total<n):
        for i in range(40):
            x = random.beta(a,b)
            r += f(x)/scipy.beta.pdf(x,a,b)
            total += 1
            m.append(r/total)
        E = Erro * r/total
        n = int((1.960**2 * np.std(m)**2) / E**2)
        #print(total,n,E,r/total,np.mean(m),np.std(m))
    plt.plot(m)
    print("Total ",total, "n ",n)

    return #retorne








def importance_sampling(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo importance sampling
    Escreva o seu codigo nas proximas linhas
    """
    #Estimação Inicial de n
    n = 40
    r = 0
    a = 1
    b = 2
    total = 0
    m = []
    while(total<n):
        for i in range(40):
            x = np.random.beta(a,b)
            r += f(x)/stats.beta.pdf(x,a,b)
            total += 1
            m.append(r/total)
        E = Erro * r/total
        n = int((1.960**2 * np.std(m)**2) / E**2)
        #print(total,n,E,r/total,np.mean(m),np.std(m))
    plt.plot(m)
    print("Total ",total, "n ",n)

    return r/total


    return #Retorne sua estimativa






def main():
    #Coloque seus testes aqui
    y = []
    x = []
    b = []
    tam = 1000
    for i in range(tam):
        y.append(f(i/tam))
        x.append(i/tam)
        b.append(stats.beta.pdf(i/tam,1,3))
    plt.plot(x,y,label="f(x)")
    plt.plot(x,b,label="beta")
    plt.show()

    plt.hist(np.random.beta(1,2,tam*1000),label="beta")
    plt.show()
    
    plt.hist(np.random.gamma(1,6,tam*1000),label="beta")
    plt.show()
    #print(y)
    print(crude())
    print(hit_or_miss())
    #print(control_variate())
    print(importance_sampling())




if __name__ == "___main__":
    main()

main()
