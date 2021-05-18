#prime or not

def prime(n):
    for i in range(2, (n // 2)):
        if n % i == 0:
            print(n, "is not a prime number")
            return
    print(n, "is a prime number")
prime(int(input()))
