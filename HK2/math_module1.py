def factors(n):
    factors_list = []
    for i in range(1, n+1):
        if n % i == 0:
            factors_list.append(i)
    return factors_list

def primes(n):
    primes_list = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(i)
    return primes_list
