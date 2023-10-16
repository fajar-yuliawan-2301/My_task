def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int (num**0.5) + 1):
        if num % i == 0:
            return False
    return True

limit = 100
number = 2

print("Bilangan prima antara 0 dan", limit, "adalah:")
while(number <= limit):
    if is_prime(number):
        print(number)
    number += 1
