def binary(arr, e, ub): #e = eleent, up= upper bound
    lb = 0 #lower bound

    while lb <= ub:
        m = (lb+ub)//2
        if e > arr[m]:
            lb = m+1
        elif e < arr[m]:
            ub = m-1
        else:
            return m
    return -1

n = int(input())
arr = [int(i) for i in input().split()]
m = int(input())
seach_arr = [int(i) for i in input().split()]



output = list()
for i in seach_arr:
    value = binary(arr,i,n-1)
    output.append(value)

print(' '.join([str(i) for i in output]))