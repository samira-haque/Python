i = 1
while i <=5:
    print(i)
    if(i == 3):
        break
    i += 1


print("End of LOOP")

#continue

i = 0
while i <=5:
    if(i==3):
        i +=1
        continue #skip
    print(i)
    i += 1