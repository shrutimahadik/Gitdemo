
#itemincart=0;
#if itemincart !=2:
    #raise Exception("exception occure")
    #pass

#assert (itemincart==2)

try:
    with open('file.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)




finally:
    print("will work always")






