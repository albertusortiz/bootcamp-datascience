import numpy as np

# Arreglo random
a = np.random.randint(0, 10, 20)

a
array([5, 1, 4, 0, 0, 3, 3, 7, 6, 2, 5, 2, 2, 6, 3, 9, 7, 5, 2, 6])

# Subarreglo de la posicion 0 a la 5
a[:5]
array([5, 1, 4, 0, 0])

# Subarreglo de la posicion 5 hasta el final
a[5:]
array([3, 3, 7, 6, 2, 5, 2, 2, 6, 3, 9, 7, 5, 2, 6])

# Subarreglo de la posicion 5 hasta el final en saltos de 2
a[5::2]
array([3, 7, 2, 2, 6, 9, 5, 6])

