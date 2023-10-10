class petStore:
    def _init_(self):
        self.pets = {
            "Dog" : [],
            "Cat" : [],
            "Rabbit" : [],
            "Parrot" : []
        }
    def storePet(self,type,breedName,price,age):
        temp = {
            "breedName" : breedName,
            "price" : price,
            "age" : age,

        }
        self.pets[type].append(temp)
P=petStore()        
print(P.pets)
P.storePet("Dog","pomerian","5000","4")
print(P.pets)
P.storePet("Cat","persian","6000","3")
print(P.pets)
P.storePet("Dog","labrador","5500","4")
print(P.pets)
     
for i in P.pets:
    print(i)
    print(P.pets[i])
    for item in P.pets[i]:
        print(item["breedName"])