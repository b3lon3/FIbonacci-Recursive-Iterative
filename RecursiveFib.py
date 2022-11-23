import numpy as np
import matplotlib.pyplot as plt
import time
from random import randint, shuffle
import math

grafico = []
tempo_final = 0 
tempo = []

def recur_fibo(n):
   
   if n <= 1:
       return n
   else:
       
       return(recur_fibo(n-1) + recur_fibo(n-2))
   
for i in range(30):
   tempo_inicio = time.time() 
   print(recur_fibo(i))
   tempo_final = time.time() - tempo_inicio
   tempo.append(tempo_final)
   grafico.append(recur_fibo(i))

plt.plot(grafico)
print(sum(tempo))