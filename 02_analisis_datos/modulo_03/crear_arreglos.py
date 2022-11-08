import numpy as np

# Crea un arreglo de 0 a 99.
np.arange(0, 100)

# Crea un arreglo de 0 a 19.
np.arange(0, 20)

# Crea un arreglo de 0 a 19 en saltos de 2 en 2.
np.arange(0, 20, 2)

# Creando un arreglo con 10 ceros.
np.zeros(10)

# Creando un arreglo de 10 ceros de tipo INT.
np.zeros(10, dtype=int)

# Creando arrays de unos.
np.ones(10, dtype=int)

# Arreglo basura
np.empty(10)

# Arreglo basura de tipo INT
np.empty(10, dtype=int)

# Arreglo entero aleatorio
np.random.randint(0, 10, 50)