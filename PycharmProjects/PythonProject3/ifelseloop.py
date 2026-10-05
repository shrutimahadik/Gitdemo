
greeting="hello good morning"

if greeting=="hello good morning":
    print("matches with the msg")
else:
    print("no matches with the msg")


#for loop
obj=[2,3,4,5,9]
for i in obj:
   #print(i)
   print(i*2)


#sumation
sumation=0
for j in range (1,6):
    sumation=sumation+j
print(sumation)

#for difference of two index
for k in range(1,10,2):
    print(k)

#similarly for index difference of 5
for a in range (1,10,5):
    print(a)

#for not mentioning staring range python will take index from 0
for m in range(10):
    print(m)
