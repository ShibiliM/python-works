no=int(input("enter a number"))
cpy=no
s=0
while(no!=0):
    r=no%10
    s=s+(r**3)
    no=no//10
if cpy==s:
    print("armstrong")
else:
    print("not rmstrong")