import random
import time

def monte_carlo_pi(n):
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return (4 * inside) / n

start = time.time()
pi_estimate = monte_carlo_pi(1_000_000)
end = time.time()

print(f"Estimativa de π: {pi_estimate:.6f}")
print(f"Tempo de execução: {end - start:.4f} segundos")
