array1 = list(map(int, input().split()))
numbers =  list(map(int, input().split()))

left = 0
answer = 0
result = 0
maximum = 0
for right in range(len(numbers)):
    answer += numbers[right]

    while left <= right and  answer > array1[1]:
        answer -= numbers[left]
        left += 1
        
    if answer <= array1[1]:
        maximum += (right - left + 1)
    
print(maximum)
