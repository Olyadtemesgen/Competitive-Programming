t = int(input())

for rr in range(t):

    n, m = list(map(int, input().split()))
    result = []
    answer = 0
    for x in range(n):
        result.append(list(map(int, input().split())))
    
    rtl = {}
    ltr = {}
    for row in range(n):

        for col in range(m):
            res = 0
            #from left to right upward
            if row == 0 or col == 0:
                r = row
                c = col
                
                while r + 1 and c + 1:
                    res += result[r][c]
                    r -= 1
                    c -= 1
                
                r = row + 1
                c = col + 1
                #from left to right downward
                while r < n and c < m:
                    res += result[r][c]
                    r += 1
                    c += 1
                
                ltr[(row, col)] = res
                res = 0
            #from right to left upward
            if col == 0 or row == n - 1:
                r = row 
                c = col
                while r + 1 and c < m:
                    res += result[r][c]
                    r -= 1
                    c += 1
                
                #from right to left downward
                r = row + 1
                c = col - 1
                while r < n and c + 1:
                    res += result[r][c]
                    r += 1
                    c -= 1
                if col == m - 1 and row != n - 1:
                    rtl[(row, 0)] = res
                else:
                    rtl[(row, col)] = res
    ans = 0
    for rows in range(n):
        
        for cols in range(m):
            answer = 0
            row = rows
            col = cols
            row2 = rows
            col2 = cols
            minimum = 0
            # if row >= m or col >= m:
            minimum = min(n - 1 - row, col)
            # print(row, col)
            answer += rtl[(row + minimum, col - minimum)]
            # print(row + minimum, col - minimum)
            minimum = min(col, row)
            # print(row - minimum, col + minimum)
            # print(answer)
            answer += ltr[(row - minimum, col - minimum)]
            answer -= result[row][col]



            # print('before', row, col)

            # print(row2, col2)
            ans = max(answer, ans)
    # print(ltr)
    # print(rtl)
    print(ans)
