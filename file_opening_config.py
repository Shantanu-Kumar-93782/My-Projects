f = open("aisehi.txt", "r")
for i, line in enumerate(f):
    if i >= 15:
        print(line.rstrip())
    if i >= 25:
        break
