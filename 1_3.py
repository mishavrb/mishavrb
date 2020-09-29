from random import randint

myfile = open("1_3","a")
for i in range(0,999):
    a = randint(0,1000)
    myfile.write(str(a))
    myfile.write(" ")
    if a%2==0 or a%3==0 or a%5==0 or a%10==0:
        myfile.write(str(a))
        myfile.write(" ")
myfile.close()