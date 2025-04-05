function sieve(n)
    primes = trues(n)
    primes[1] = false
    for i in 2:floor(Int, sqrt(n))
        if primes[i]
            for j in i*i:i:n
                primes[j] = false
            end
        end
    end
    return findall(primes)
end

@time result = sieve(1_000_000)
println("Total de primos: ", length(result))
