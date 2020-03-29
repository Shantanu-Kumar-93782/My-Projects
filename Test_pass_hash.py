import hashlib
pass_size = 5
file_ka_pointer = open('pass.txt', 'r')
print(file_ka_pointer.tell())
l=input("Enter your Hash")
content = file_ka_pointer.readlines()
for i in content:
    if l == str((hashlib.md5((i.rstrip()).encode())).hexdigest()):
        print(i[:pass_size] + " and its hash" + str((hashlib.md5(i[:pass_size].encode())).hexdigest()))
        break
    
        
 