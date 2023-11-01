# x=lambda a,b: a*b
# print(x(5,10))

# list1=[1,2,3,4,5,6,7,8,9,10]
# evennumbers=list(filter(lambda x : x%2==0,list1))
# oddnumbers=list(filter(lambda y: y%2!=0,list1))
# print("even numbers",evennumbers)
# print("odd numbers",oddnumbers)


# list1=[1,2,3,4,5,6,7,8,9,10]
# squerenumber=list(map(lambda x:x**2,list1))
# cubenumber=list(map(lambda y:y**3,list1))
# print("squere number",squerenumber)
# print("cube number",cubenumber)



# list1=[-1,2,-3,5,7,8,9,-10]
# y=[]
# rarngdary=list(filter(lambda x: (x>0),list1))
# rarn=list(filter(lambda z: (z<0),list1))
# y=rarngdary+rarn
# print("rearranged array",y)


# originallist=[1,2,3,5,7,8,9,10]
# evennumbers=len(list(filter(lambda x:x%2==0,originallist)))
# oddnumbers=len(list(filter(lambda y:y%2!=0,originallist)))
# print("number of even numbers",evennumbers)
# print("numbers of odd number",oddnumbers)

list=[1,2,3]
list2=[4,5,6]
result=list(map(lambda x,y: x+y ,list,list2))
print("added list",result)