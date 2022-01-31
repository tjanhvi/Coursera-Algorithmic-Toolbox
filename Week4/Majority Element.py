n = int(input())
seq = [int(i) for i in input().split()]

def majority_element(seq, left, right):
    if left+1 == right:
        return seq[left]
    elif left+2 == right:
        return seq[left]

    mid = (left+right)//2
    l = majority_element(seq, left, mid)
    r = majority_element(seq, mid, right)

    c1, c2 = 0, 0
    for i in seq[left:right]:
        if i == l:
            c1+=1
        elif i == r:
            c2+=1
    if c1>(right-left)//2 and l != -1:
        return l
    elif c2>(right-left)//2 and r != -1:
        return r
    else: 
        return -1

print(int(majority_element(seq, 0, n) != -1))
    
    
