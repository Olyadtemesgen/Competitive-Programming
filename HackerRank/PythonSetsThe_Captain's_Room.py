n = int(input())
arr = input()
arr = arr.split()
dict = {}
for ar in arr:
    dict[ar] = dict.get(ar, 0) + 1
for ar in arr:
    if dict[ar] == 1:
        print(int(ar))
        break
