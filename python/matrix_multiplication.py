import numpy as np
import time

# Criação de matrizes 1000x1000
A = np.random.rand(1000, 1000)
B = np.random.rand(1000, 1000)

start_time = time.time()
C = np.dot(A, B)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
