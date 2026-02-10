def factorial(n):
    factors = []
    fact = 1
    for i in range(1, n+1):
        fact *= i
        factors.append(fact)
    return factors
print(factorial(5))