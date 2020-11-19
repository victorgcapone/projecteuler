from math import sqrt, ceil


def largest_prime_factor(number):
    start = int(sqrt(number))+1
    for i in range(start, 2, -1):
        if number % i == 0 and is_prime(i):
            return i


def is_prime(number):
    end = int(sqrt(number))+1
    for i in range(2, end):
        if number % i == 0:
            return False
    return True

print(largest_prime_factor(600851475143))