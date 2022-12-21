n = int(input())
arr = []
for x in range(n):
    arr.append(input())
dict = {}
for ar in arr:
    dict[ar] = dict.get(ar, 0) + 1
print(len(dict))
for x in dict:
    print(dict[x], end = ' ')
