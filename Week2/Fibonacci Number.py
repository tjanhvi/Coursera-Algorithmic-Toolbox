num = int(input())

if num <=1:
    print(num)
    quit()

def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a,b = b, a+b
    return a
print(fibonacci(num))