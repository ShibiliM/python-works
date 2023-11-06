class circle():
   
    def __init__(self,r):
        self.r=r
        self.pi=3.14
    def area(self):
        circarea=self.pi*(self.r**2)
        print(circarea)
    def circumfrence(self):
        circcrcmfrce=2*(self.pi*self.r)
        print(circcrcmfrce)
crcle=circle(3)
crcle.area()
crcle.circumfrence()