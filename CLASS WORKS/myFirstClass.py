class MSCDSB:
     
    def __init__(self):
        # data members / properties / attributes
        self.name = "MSC DS B"
        self.students = ["A","B","C"]

    def printStudents(self): # member function
        for student in self.students:
            print(student)

    
obj = MSCDSB()
print(obj.name,obj.students)
obj.printStudents()


