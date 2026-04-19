x = input()
output = ""
for i in range(len(x)):
    if i == 0 and (9-int(x[0])) == 0:
        output += x[0]
    else:
        output += str(min(int(x[i]), 9-int(x[i])))
print(output)
