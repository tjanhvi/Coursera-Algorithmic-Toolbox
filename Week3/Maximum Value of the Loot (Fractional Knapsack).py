n, W = map(int, input().split())
list = []

if W == 0:
    print(0)
    quit()

for i in range(n):
    v, w = [int(i) for i in input().split()]
    if v == 0:
        continue
    list.append((v,w))
    
list.sort(key = lambda x: x[0]/x[1], reverse=True)

total = 0

for v,w in list:
    if w == 0:
        print(total)
        quit()
    value = min(w,W)
    total += value*v/w
    W -= value

print(total)


