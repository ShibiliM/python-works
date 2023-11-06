class heat():
    def __init__(self):
        self.ogcelcus=float(input("enter amount of heat in celcius"))
        
    def farenheat(self):
        frheat=(self.ogcelcus*(9/5))+32
        print("heat in faren heat",frheat)
    def kelvin(self):
        klvnheat=self.ogcelcus+273.15
        print("heat in kelvin",klvnheat)
obj=heat()
obj.farenheat()
obj.kelvin()
        