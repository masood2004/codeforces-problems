matrix = []
for i in range(5):
    temp = input().split()
    temp = [int(t) for t in temp]
    matrix.append(temp)
turns = 0
location = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            if i < 2:
                turns += (2-i)
            elif i > 2:
                turns += (i-2)
            if j < 2:
                turns += (2-j)
            elif j > 2:
                turns += (j-2)

print(turns)
