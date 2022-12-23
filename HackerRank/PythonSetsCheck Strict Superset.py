A = set(input().split())
n = int(input())
sets = []

for sett in range(n):
    sets.append(set(input().split()))

for index, sett in enumerate(sets):
    if not A.issuperset(sett):
        print(False)
        break
    elif index == len(sets) - 1:
        print(True)
