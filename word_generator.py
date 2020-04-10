import math

size = int(input())
my_indices = list('abcdefghijklmnopqrstuvwxyz0123456789')
to_find = float(input())
my_word = ''

for i in range(size):
    current = to_find%36
    if current == math.floor(current):
        my_word += my_indices[int(current)-1]
        print("here1")
    elif current > math.floor(current):
        my_word += my_indices[int(math.ceil(current))-1]
        print("here2")
    else:
        pass
    to_find = to_find/36
my_word = list(my_word)
my_word.reverse()
my_word = "".join(my_word)
print(my_word)

