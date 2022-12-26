# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

a = input().split()
n = (a[0])
n = int(a[0])
m = int(a[1])
A = []

counter = defaultdict(list)

for ab in range(n):
    abb = input()
    A.append(abb)

for idx, char in enumerate(A):
    counter[char].append(str(idx + 1))
B = [] 
for b in range(m):
    B.append(input())
for a in B:
    if a in A:
        print(' '.join(counter[a]))
    
    else:
        print('-1')
