def calculateSum(n) :
    if (n <= 0) :
        return 0
  
    fibo =[0] * (n+1)
    fibo[1] = 1
    
    # Initialize result
    sum = (fibo[0] * fibo[0])+(fibo[1] * fibo[1])
  
    arr= []
    # Add remaining terms
    for i in range(2,n+1) :
        fibo[i] = fibo[i-1] + fibo[i-2]
        sum = sum + (fibo[i]*fibo[i])
        arr.append(sum)
        listToStr = ' '.join([str(elem) for elem in arr])
    print(listToStr[-1])

n = int(input())
calculateSum(n)

