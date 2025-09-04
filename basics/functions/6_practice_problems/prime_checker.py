def is_prime(n):
    if n < 2:                 #below 2 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(12))  # False


# 5 is a prime number because it can only be divided by 1 and 5