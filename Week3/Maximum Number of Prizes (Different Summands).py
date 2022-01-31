n = int(input())

if n == 1:
    print(1)
    print(1)
    quit()

w = n
prizes = []
for i in range(1,n):
    if w>2*i:
        prizes.append(i)
        w -= i
    else:
        prizes.append(w)
        break

print(len(prizes))
print(' '.join([str(i) for i in prizes]))