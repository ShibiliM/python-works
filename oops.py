class student():
    def __init__(self,name,rollno,sub,mark):
         self.name=name
         self.rollno=rollno
         self.sub=sub
         self.mark=mark
c1=student("binu",19,"maths",22)
print(c1.name,c1.rollno,c1.sub,c1.mark)
c1.mark=25
print(c1.mark)