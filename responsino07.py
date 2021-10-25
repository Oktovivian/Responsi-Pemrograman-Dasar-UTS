bilangan = int(input())

#while i <= bilangan:
    #if bilangan % 2 == 0:
        #print(i, "adalah genap")
    #else:
        #print(i,"adalah ganjil")
    #i = i+1

for i in range(1,bilangan+1):
    if i % 2 == 0:
        print(i, "adalah genap")
    elif i % 2 != 0:
        print(i,"adalah ganjil")
