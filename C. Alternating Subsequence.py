t = int(input())

for x in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    pointer = False
    left = 0
    right = 0
    answer = 0

    while right < len(array):
        
        while right < len(array) and array[left] * array[right] > 0:
            if array[left] < array[right]:
                left = right
            
            right += 1
    
        answer += array[left]
        left = right
    
    print(answer)
