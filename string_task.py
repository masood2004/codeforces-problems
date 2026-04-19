word = input()
# word = 'Codeforces'
vowels = "aeiouyAEIOUY"
charcters = [c for c in word]
temp = []
for c in charcters:
    if not c in vowels:
        temp.append('.')
        temp.append(c.lower())
temp_string = ""
for t in temp:
    temp_string += t
print(temp_string)
