m, n, a = map(int,input().split())
abc = list(map(lambda x : x // a if x % a == 0 else x // a + 1, [m, n]))
print(abc[0] * abc[1])
