#multiplication table
def multiplication(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
        
n = int(input())
multiplication(n)
