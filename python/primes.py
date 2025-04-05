import time

def sieve(n):
    primes = [True] * (n + 1)
    primes[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i, prime in enumerate(primes) if prime]

start = time.time()
result = sieve(1000000)
end = time.time()

print(f"{len(result)} primos encontrados em {end - start:.4f} segundos")
