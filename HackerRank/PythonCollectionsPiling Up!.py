# Enter your code here. Read input from STDIN. Print output to STDOUT
#I use the two pointer algorithm with time complexity O(n)
T = int(input())

for x in range(T):
    
    n = int(input())
    blocks = list(map(int, list(input().split())))
    left = 0
    right = n - 1
    upper_pile = max(blocks[left], blocks[right])
    while left < right:
        if upper_pile < max(int(blocks[left]), int(blocks[right])):
            print('No')
            break
        elif int(blocks[left]) > int(blocks[right]):
            upper_pile = int(blocks[left])
            left += 1
            
        elif blocks[left] < blocks[right]:
            upper_pile = blocks[right]
            right -= 1
        else:
            if blocks[left + 1] > blocks[right]:
                upper_pile = blocks[left]
                left += 1
            
            else:
                upper_pile = blocks[right]
                right -= 1
            
        if right == left:
            print("Yes")
