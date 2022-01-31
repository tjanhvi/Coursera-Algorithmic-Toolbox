n = int(input())

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort()

value = sum([a[i]*b[i] for i in range(n)])
print(value)
