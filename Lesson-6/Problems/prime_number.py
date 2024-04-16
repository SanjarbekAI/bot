"""
cheksiz tub sonlarni qaytarib beradigan generator yozing
"""


def prime_generator():
    yield 2
    number = 3
    primes = [2]
    while True:
        is_prime = True
        for prime in primes:
            if prime * prime > number:
                break
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
            yield number
        number += 2


for num in prime_generator():
    print(num)
