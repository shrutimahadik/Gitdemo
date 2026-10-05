
it=4
while it>1:
    print(it)
    it=it-1
print(it)
print("********")

#in above code if i dont want  3 to print in output then code will be
it=4
while it>1:
    if it==3:
        break

    print(it)
    it=it-1

#similarly for it=10 and dont want 3 in output code will be
it=10
while it>1:
    if it==3:
        break
    print(it)
    it=it-1
print("#############")

#continue
#similarly for it=10 and dont want 3 in output code will be
it=10
while it>1:
    if it==9:
        it=it-1
        continue
    if it==3:
        break
    print(it)
    it=it-1