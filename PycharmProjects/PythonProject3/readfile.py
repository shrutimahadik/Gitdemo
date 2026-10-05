
file=open('text.txt')
#print(file.read())    #use to read all content of file

#print(file.read(2))
#print(file.readline()) #one read line at a time
#print(file.readline())

#file.close()

#print line by line using readline method
#line=file.readline()
#while line!="":
    #print(line)
    #line=file.readline()
#file.close()

#readlines method
#values read in list [shruti mahadik ganesh kunjir]

for line in file.readlines():
    print(line)
