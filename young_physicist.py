n = int(input())
forces = []
for i in range(n):
    vector = input().split()
    vector = [int(v) for v in vector]
    forces.append(vector)

x_axis = 0
y_axis = 0
z_axis = 0

for i in range(n):
    x_axis += forces[i][0]
for i in range(n):
    y_axis += forces[i][1]
for i in range(n):
    z_axis += forces[i][2]

if x_axis == 0 and y_axis == 0 and z_axis == 0:
    print("YES")
else:
    print("NO")
