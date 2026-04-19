n = int(input())

value = 0
for i in range(n):
    statement = input()
    if (statement[0] == "+" and statement[1] == "+") or (statement[-1] == "+" and statement[-2] == "+"):
        value += 1
    elif (statement[0] == "-" and statement[1] == "-") or (statement[-1] == "-" and statement[-2] == "-"):
        value -= 1

print(value)
