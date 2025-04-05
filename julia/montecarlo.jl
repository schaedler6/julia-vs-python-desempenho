using Random

function monte_carlo_pi(n)
    inside = 0
    for _ in 1:n
        x, y = rand(), rand()
        if x^2 + y^2 <= 1
            inside += 1
        end
    end
    return 4 * inside / n
end

@time pi_estimate = monte_carlo_pi(1_000_000)
println("Estimativa de π: ", pi_estimate)
