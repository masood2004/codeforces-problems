n, l = map(int, input().split())

a = list(map(int, input().split()))
list.sort(a)

first_edge = abs(0 - a[0])
last_edge = l - a[n-1]
gaps_between_lanterns = []
for i in range(n-1):
    gaps_between_lanterns.append((a[i+1] - a[i])/2)

print(max(first_edge, last_edge, max(gaps_between_lanterns)))
