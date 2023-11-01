no=int(input("eneter a number"))
count=0
i=1
while(i<=no):
    if no%i==0:
        count+=1
    i+=1
if count==2:
    print("number is prime")
else:
    print("number not prime")
