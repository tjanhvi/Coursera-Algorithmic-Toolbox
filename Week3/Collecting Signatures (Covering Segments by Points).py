n = int(input())
list1 = []
list2 = []
for i in range(n):
    a, b = map(int, input().split())
    list1.append((a))
    list2.append((b))
    list1.sort(reverse=True)
    list2.sort(reverse=True)

print(list1[-1])
print(list2[-1])






