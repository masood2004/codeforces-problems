n_and_k = input().split()
n = int(n_and_k[0])
k = int(n_and_k[1])

scores = input().split()
scores = [int(s) for s in scores]

threshold = scores[k-1]

count = 0
for s in scores:
    if s >= threshold and s > 0:
        count += 1

print(count)
