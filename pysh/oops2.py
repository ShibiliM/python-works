class area():
    def __init__(self,a,b,h):
        self.a=a
        self.b=b
        self.h=h
    def squre(self):
        sqrarea=self.a*self.a
        print(sqrarea)
    def rect(self):
        recarea=self.b*self.h
        print(recarea)
    def triangle(self):
        trianarea=0.5*self.b*self.h
        print(trianarea)
ar=area(3,2,5)
ar.squre()
ar.rect()
ar.triangle()

        