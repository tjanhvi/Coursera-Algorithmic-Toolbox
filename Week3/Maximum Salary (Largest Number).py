n = int(input())

a = [int(i) for i in input().split()]

a.sort(reverse=True)
listToString = ''.join([str(j) for j in a])
print(listToString)