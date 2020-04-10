count = 0
for i in numbers:
    if i%3==0 and i%5==0:
        current = sum(list(map(int, list(str(i)))))
        print (i)
        print(current)
        if current%4!=0:
            count+=1
return count