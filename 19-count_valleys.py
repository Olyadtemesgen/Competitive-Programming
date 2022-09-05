def countingValleys(steps, path):
    num = 0
    list = []
    for x in path:
        if x == "U":
            num += 1
            list.append(num)
        else:
            num -= 1
            list.append(num)
    counter = 0
    for x in range(1 , steps):
        if list[x] == 0 and list[x - 1] < 0:
            counter += 1
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
