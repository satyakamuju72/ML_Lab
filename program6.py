#greatest of three

a = int(input())
b = int(input())
c = int(input())
res = a
if(res < b):
    res = b
if(res < c):
    res = c
print(res, "is the greatest number")
