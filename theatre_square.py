values = input().split()
values = [int(v) for v in values]

# print(values)


ceiling_n = (values[0] + values[2] - 1) // values[2]
# print(ceiling_n)

ceiling_m = (values[1] + values[2] - 1) // values[2]
# print(ceiling_m)

total_blocks = ceiling_n * ceiling_m

print(total_blocks)
