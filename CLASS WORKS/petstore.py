#create a petstore class where you have the details of pets available and their details.
#The class will have methods
# - store a new pet details
# - serach for a pet
# - sell a pet
# - list all pets

# importing your petstore class, create a petstoremain file, where you will implement a menudriven program for admin 
# who will manage the store & use who will  see the pets and buy pets.
class pet_store:
    def __init__(self):
        self.pet ={
            "dogs":[],
            "cats":[],
            "rabbits":[],
            "parrots":[]
        }
        
    def addPet(self,name,id,breed):
        self.pet.append( {
            "Name" : name,
            "id" : id,
            "Breed": breed
        })
    
    def searchPet(self,name,breed):
        pass
        
        
    def sellPet(self,name,price):
        pass
    
    
    def listpet(self,name,id,breed,price,year):
        pass
    
    while True:
        print("Menu Options")
        print("1. Add a new Pet")
        print("2. Serach a Pet")
        print("3. Sell a Pet")
        print("4. List all Pets")
        print("5. Exit")

        choice = input("Enter the choice").strip()
        if choice == "1":
            name,id,breed = addPet()
            # createStudent(name, regno, email, phone)
        elif choice == "2":
            searchPet()
        elif choice == "3":
            sellPet()
        elif choice == "4":
            listpet()
        elif choice == "5":
            exit()
        else:
            print("Invalid Choice")