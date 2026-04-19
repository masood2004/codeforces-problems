from collections import Counter
n = 2
a = [3, 3, 4, 5, 3, 3]
b = []

s = Counter(a)
if s.most_common()[0][1] == 1:
    print("NO")
else:
    sorted_a = sorted(a)
    for i in range((len(sorted_a)//2), len(sorted_a)-1):
        popped = a.pop(i)
        print(popped)

    print(a)
    print(b)
    # for i in range(n):
    #     while True:
    #         try:
    #             a = set(map(int, input().split()))
    #             if len(a) % 2 == 0 and len(a) != 0:
    #                 print('good')
    #                 break
    #             else:
    #                 print("Even number of Input Required")
    #         except ValueError:
    #             print("Invalid error")
