class area():
    def __init__(self,a,b,h):
        self.a=a
        self.b=b
        self.h=h
class squaere(area):
    
      def sqre(self):
        area=self.a*self.a
        print(area)
class recarea(squaere):
   
      def rec(self):
        rectaraea=self.b*self.h
        print(rectaraea)
class triangle(recarea):
  
      def triaarea(self):
        triarea=0.5*self.b*self.h
        print(triarea)
obj=triangle(2,3,4)
obj.sqre()
obj.rec()
obj.triaarea()
    
