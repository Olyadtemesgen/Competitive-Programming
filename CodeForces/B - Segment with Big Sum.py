array1 = list(map(int, input().split()))
numbers =  list(map(int, input().split()))

left = 0
summ = 0
answer = float("inf")

for right in range(len(numbers)):
    
    summ += numbers[right]

    while left <= right and summ >= array1[1]:

        summ -= numbers[left]
        answer += right - left + 1)
        left += 1

if answer == float("inf"):
    print(-1)

else:
    print(answer)
