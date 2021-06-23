import numpy as np

lista = [np.random.randint(20) for i in range(20)]

def es_primo(num):
    contador = 0
    for i in range(1, num+1):
        if num % i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False

primos = list(filter(es_primo, lista))
print(primos)
