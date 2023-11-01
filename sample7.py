no=int(input("enter series"))
b=1
c=0 
i=0
while(i<no):
    print(c,end=" ")
    a=b
    b=c
    c=a+b
    i+=1
