#Solving the maximum pairwise product programming challenge
n = int(input())
a = [int(x) for x in input().split()]

def Maximum_pairwise_product(arr):
    arr = sorted(arr)
    assert(len(arr) == n)
    print(arr[n-1]*arr[n-2])

Maximum_pairwise_product(a)
