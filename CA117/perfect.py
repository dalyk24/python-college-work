#!/usr/bin/env python3

def checker(m):
    try:
        return int(m)
    except ValueError:
        print("Please Enter Positive Integer")
        quit()

def get_divisors(n):
    n = checker(n)
    divisors = []
    i = 1
    while i <= n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return sorted(divisors)

def get_proper_divisors(m):
    m = checker(m)
    pdivisors = get_divisors(m)
    pdivisors.remove(m)
    return pdivisors

def is_perfect(n):
    n = checker(n)
    fdivisors = get_proper_divisors(n)
    summ = sum(fdivisors)
    if summ == n:
        return True
    else:
        return False
