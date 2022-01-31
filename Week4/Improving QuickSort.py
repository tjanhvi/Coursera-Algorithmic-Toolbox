import random
import time
def quicksort3(arr, l, r):

    if l + 1 >= r:
        return

    m = random.randint(l, r-1)
   
    arr[l], arr[m] = arr[m], arr[l]

    # partition procedure
    m1, m2 = partition3(arr, l, r)

    quicksort3(arr, l, m1)
    quicksort3(arr, m2+1, r)

def partition3(arr, l, r):
    m2 = l
    for i in range(l+1, r):
        if arr[i] <= arr[l]:
            arr[m2+1], arr[i] = arr[i], arr[m2+1]
            m2 += 1

    arr[l], arr[m2] = arr[m2], arr[l]

    m1 = l
    for i in range(l, m2):
        if arr[i] < arr[m2]:
            arr[i], arr[m1] = arr[m1], arr[i]
            m1 += 1
    return m1, m2

def create_array(size):
    return [random.choice(list(range(10))) for _ in range(size)]


n = int(input())
seq = [int(i) for i in input().split()]
quicksort3(seq, 0, 100000)
for x in seq:
    print(x, end=' ')


