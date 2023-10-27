
class car:
    def __init__(self,mfg,mdl,year):
        self.Manufacturer = mfg
        self.Model = mdl
        self.Year = year
        
bmw = car("BMW","F series",2020)
print(bmw.Manufacturer)    

ferari = car("Ferari","A series",2023)
print(ferari.Model)    