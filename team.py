# n = int(input("Enter the number of problems: "))
n = int(input())
count = 0
for i in range(n):
    while True:
        solvable = input()
        # solvable = input(
        #     f"Write 1 or 0 and SPACE after it to Vote for {i}th problem: ")

        votes = solvable.split()

        if len(votes) == 3 and all(v in ('0', '1') for v in votes):
            vote_list = [int(v) for v in votes]
            break

    if sum(vote_list) >= 2:
        count += 1
print(count)
