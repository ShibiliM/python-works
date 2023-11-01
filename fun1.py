# def maxi(a,b,c):
#     print(max(a,b,c))
# maxi(5,1,2)


# def sumlstnmbrs(numbers):
#     total=sum(numbers)
#     return total
# samplelist=[8,2,3,0,7]
# result=sumlstnmbrs(samplelist)
# print("sum of numbers in sample list   :",result)

# def sumlstnmbrs(numbers):
#     result=1
#     for i in numbers:
#         result*=i
#     return result
# samplelist=[8,2,3,-1,7]
# result=sumlstnmbrs(samplelist)
# print("multiply of numbers in sample list   :",result)


# def unique(inputlist):
#     for i in inputlist:
#         if i not in list1:
#             list1.append(i)
#     return list1
# list=[1,2,3,3,3,3,4,5]
# list1=[]
# list1=unique(list)
# print("unique list",list1)


# def even_numbers(numbers):
#     for i in numbers:
#         if i%2==0:
#             list1.append(i)
#     return list1
# list=[1,2,3,4,5,6,7,8,9]
# list1=[]
# list1=even_numbers(list)
# print("even numbers list  :",list1)


def palindrom(input_string):
    cpystring=input_string.replace(" "," ").lower()
    return cpystring==cpystring[::-1]
sample_string="hello"
if palindrom(sample_string):
    print("string is plaindrome")
else:
    print("sttring not palindrome")