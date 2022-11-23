import numpy as np
import matplotlib.pyplot as plt
import time
from random import randint, shuffle
import math

grafico = []
tempo_final = 0 
tempo = []

def fib(n):
    
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
  
    return a

for i in range(30):
    tempo_inicio = time.time() 
    print(fib(i))
    tempo_final = time.time() - tempo_inicio
    tempo.append(tempo_final)
    grafico.append(fib(i))

plt.plot(grafico)
print(sum(tempo))
