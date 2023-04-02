import math

saved = list(map(int, input().split()))

# g_c_d = math.gcd(saved[0], saved[1])
difference = saved[1] - saved[0]

if difference == 0:
    print(saved[0])
    
elif difference == 1:
    print(math.gcd(saved[0], saved[1]))
else:
    print(1)
