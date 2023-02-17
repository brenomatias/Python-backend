import array as arr
import numpy as np

# evitar usar
arr.array('d', [1, 3.5])

# evitaremos usar array puro,se precisamos de trabalho numérico, é costume usar o numpy
numeros = np.array([1, 3.5])
print(numeros+3)