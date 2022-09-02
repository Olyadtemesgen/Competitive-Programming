def gradingStudents(grades):
    # Write your code here
    new_g = []
    for i in range(len(grades)):
        if grades[i] < 38:
            new_g.append(grades[i])
        elif grades[i] % 5 >= 3:
            new_g.append((grades[i] - grades[i] % 5 + 5))
        else:
            new_g.append(grades[i])
    return new_g

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
