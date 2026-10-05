#read the file and store all the lines in list
#reverse the list
#write the list back to file

with open('text.txt','r') as reader:
    content=reader.readlines()   #[shruti , mahadik, ganesh ,kunjir]
    reversed(content) #[kunjir ganesh mahadik shruti]

    with open('text.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)

