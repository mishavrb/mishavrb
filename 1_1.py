a=0
b=1
c=0
myfile = open("1_1numbers.txt","w")
myfile.write(str(a))
myfile.write(" ")
myfile.write(str(b))
myfile.write(" ")
b=a+b
for i in range(0,26):
    myfile.write(str(b))
    myfile.write(" ")
    c=b
    b=c+a
    a=c
myfile.close()