import math
t = int(input())

for x in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    aa = False
    
    total = 0

    indexs = int(math.log2(n))

    for x in range(indexs):
        
        difference = 2 ** (x)
     
        for index in range(difference, n, difference * 2):
            
            if array[index] < array[index - difference]:
                temp = index - difference
                indexss = index
                
                while temp < indexss:
                    array[temp], array[index] = array[index], array[temp]
                    index  += 1
                    temp += 1
                
                total += 1
        
        answer = False

    for x in range(1, n):

        if array[x] <= array[x - 1]:
            answer = True

    if len(array) == 1 and array[0] == 1:
        print(0)

    elif not answer:
        print(total)
        
    else:
        print(-1)
