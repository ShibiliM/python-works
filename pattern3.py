n=5
k=n*2-2
for i in range(1,n):
    for j  in range(0,k):
        print(end=" ")
    k-=1
    for x in range(1,i+1):
            print("*",end=" ")
    print()
  
        