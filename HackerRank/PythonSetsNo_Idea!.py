# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
a = a.split()
arr = input()
arr = arr.split()
set1 = input()
set1 = set(set1.split())
set2 = input()
set2 = set(set2.split())
happiness = 0
for x in range(int(a[0])):
    if arr[x] in set1:happiness += 1
    if arr[x] in set2:happiness -= 1
print(happiness)
