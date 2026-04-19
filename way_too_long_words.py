n = int(input())
for i in range(n):
    word = input()
    if len(word) > 10:
        first_letter = word[:1:]
        last_letter = word[-1::]
        other_letter = word[1:len(word)-1]
        print(first_letter + str(len(other_letter)) + last_letter)
        # print
    else:
        print(word)
