nombres_premiers = [
    num for num in range(2, 1001) if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
]

for prime in nombres_premiers:
    print(prime)
