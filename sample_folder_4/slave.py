import socket
import time
import os
import hashlib
import math
slave_socket = socket.socket()
slave_socket.connect(('127.0.0.1', 5001))

my_params = str((slave_socket.recv(2048)).decode()).split()
print(my_params)
hash_to_be_calculated = my_params[0]
hash_type_selected = int(my_params[1])
if my_params[2]=='True':
    wordlist_type = "Predefined"
else:
    wordlist_type = "Custom"


if wordlist_type == "Predefined":
    number_of_words = int(((os.popen('wc predefined_wordlist.txt -l').read()).split())[0])
else:
    if my_params[3]=='1':
        number_of_words = 26**int(my_params[4])
        my_indices = list('abcdefghijklmnopqrstuvwxyz')
    elif my_params[3]=='2':
        number_of_words = 52**int(my_params[4])
        my_indices = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    elif my_params[3]=='3':
        number_of_words = 10**int(my_params[4])
        my_indices = list('0123456789')
    elif my_params[3]=='4':
        number_of_words = 62**int(my_params[4])
        my_indices = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

if int(my_params[5])+1 != int(my_params[6]):
    my_first = (int(number_of_words/int(my_params[6]))*int(my_params[5]))+1
    my_last = (int(number_of_words/int(my_params[6]))*(int(my_params[5])+1))+1
else:
    my_first = (int(number_of_words/int(my_params[6]))*int(my_params[5]))+1
    my_last = number_of_words


if wordlist_type == "Custom":
    size = int(my_params[4])
    to_find = my_first
    my_word1 = ''
    for i in range(size):
        current = to_find%len(my_indices)
        if current == math.floor(current):
            my_word1 += my_indices[int(current)-1]
        elif current > math.floor(current):
            my_word1 += my_indices[int(math.ceil(current))-1]
        else:
            pass
        to_find = to_find/len(my_indices)
    my_word1 = list(my_word1)
    my_word1.reverse()
    my_word1 = "".join(my_word1)
    print(my_word1)

    size = int(my_params[4])
    to_find = my_last
    my_word2 = ''

    for i in range(size):
        current = to_find%len(my_indices)
        if current == math.floor(current):
            my_word2 += my_indices[int(current)-1]
        elif current > math.floor(current):
            my_word2 += my_indices[int(math.ceil(current))-1]
        else:
            pass
        to_find = to_find/len(my_indices)
    my_word2 = list(my_word2)
    my_word2.reverse()
    my_word2 = "".join(my_word2)
    print(my_word2)
    statement = str("crunch " + str(size) + " " + str(size) + " " + "".join(my_indices) + " -s " + my_word1 + " -e " + my_word2 + " > my_pass_list.txt")
    os.popen(statement).read()

if wordlist_type == "Predefined":
    print("i am here")
    f = open("predefined_wordlist.txt", "r")
    if hash_type_selected == 1:
        for i, line in enumerate(f):
            if i >= my_first:
                if hash_to_be_calculated == str((hashlib.md5((line.rstrip()).encode())).hexdigest()):
                    print(str(line.strip()) + " and its hash" + str((hashlib.md5(str(line.rstrip()).encode())).hexdigest()))
                    break
            if i > my_last:
                break
    if hash_type_selected == 2:
        for i, line in enumerate(f):
            if i >= my_first:
                if hash_to_be_calculated == str((hashlib.sha1((line.rstrip()).encode())).hexdigest()):
                    print(str(line.strip()) + " and its hash" + str((hashlib.sha1(str(line.rstrip()).encode())).hexdigest()))
                    break
            if i > my_last:
                break
    if hash_type_selected == 3:
        for i, line in enumerate(f):
            if i >= my_first:
                if hash_to_be_calculated == str((hashlib.sha256((line.rstrip()).encode())).hexdigest()):
                    print(str(line.strip()) + " and its hash" + str((hashlib.sha256(str(line.rstrip()).encode())).hexdigest()))
                    break
            if i > my_last:
                break


if wordlist_type == "Custom":
    print("i am here in custom")
    f = open("my_pass_list.txt", "r")
    line = f.readline()
    if hash_type_selected == 1:
        while line:
            if hash_to_be_calculated == str((hashlib.md5((line.rstrip()).encode())).hexdigest()):
                print(str(line.strip()) + " and its hash" + str((hashlib.md5(str(line.rstrip()).encode())).hexdigest()))
                break
            line = f.readline()
    if hash_type_selected == 2:
        while line:
            if hash_to_be_calculated == str((hashlib.sha1((line.rstrip()).encode())).hexdigest()):
                print(str(line.strip()) + " and its hash" + str((hashlib.sha1(str(line.rstrip()).encode())).hexdigest()))
                break
            line = f.readline()
    if hash_type_selected == 3:
        while line:
            if hash_to_be_calculated == str((hashlib.sha256((line.rstrip()).encode())).hexdigest()):
                print(str(line.strip()) + " and its hash" + str((hashlib.sha256(str(line.rstrip()).encode())).hexdigest()))
                break
            line = f.readline()

slave_socket.close()



### RAW CODE

#data = slave_socket.recv(1024).decode()
#starting, ending = data.split()
#os.system("crunch 4 4 -s "+starting+" -e "+ ending)


'''if self.hash_tab_radio_button_2.get_active():
            if charset==1:
                comman = "crunch "+ size +" "+ size+ " abcdefghijklmnopqrstuvwxyz > current_pass_list.txt"
                os.popen(comman).read()
            elif charset==2:
                comman = "crunch "+ size +" "+ size+ " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ > current_pass_list.txt"
                os.popen(comman).read()
            elif charset==3:
                comman = "crunch "+ size +" "+ size+ " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456890 > current_pass_list.txt"
                os.popen(comman).read()
            elif charset==4:
                comman = "crunch "+ size +" "+ size+ " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456890 > current_pass_list.txt"
                os.popen(comman).read()'''

'''#data = ""
#while data!="exit":
    #time.sleep(3)
    print("recv mai atka")
   # data = slave_socket.recv(1024).decode()
    print(str(data))
    print("input mai atka")
    #slave_socket.send(input().encode())
if str(input()):'''
