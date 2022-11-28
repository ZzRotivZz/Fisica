#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np
import math
#Escreva seu nome e numero USP
INFO = {9379548:"Vitor Gonçalves Ribeiro"}

def dentro(x,y):
    return 1 if x**2+y**2<1 else 0

def estima_pi(Seed = None):

    random.seed(Seed)
    #random.random() gera um numero com distribuicao uniforme em (0,1)
    """
    Esta funcao deve retornar a sua estimativa para o valor de PI
    Escreva o seu codigo nas proximas linhas
    """
    
    # estimativa pessimista
    # diminuir o E aumenta o n, por isso no pessimista considero pi/4 = 1/2
    pi4 = 2
    var = 1
    E = 0.05/100 * 1/2
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
                certos += dentro(x,y)
                total += 1

        pi4 = certos/total
        
        E = 0.05/100 * pi4

        sigma = (pi4)*(1-pi4)
        n = (1.960**2 * sigma) / E**2
    #print('Total ',total,' n ',n, certos,total)
    return pi4*4

#estima_pi()
#n_pi = estima_pi()
#print(n_pi, (n_pi-math.pi)/math.pi)
