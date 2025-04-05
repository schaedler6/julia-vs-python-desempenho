using Random, LinearAlgebra

A = rand(1000, 1000)
B = rand(1000, 1000)

@time C = A * B
