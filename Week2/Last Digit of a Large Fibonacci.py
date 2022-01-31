n = int(input())
fibonacci_numbers = [0, 1]
for i in range(2,n+1):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

listToStr = ' '.join([str(elem) for elem in fibonacci_numbers])
print(listToStr[-1])