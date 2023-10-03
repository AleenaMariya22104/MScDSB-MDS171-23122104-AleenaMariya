class Stack:
    def __init__(self):
        self.items = []
     
     
    # push item
    def push(self, item):
        self.items.append(item)
        print(self.items)
    
    
    
    # pop item    
    def pop(self, item):
        self.items.pop(item)
        print(self.items)
        return item
        
    # print items in the stack
    def view (self):
        print(self.items)
    
    # size of the stack
    def size (self):
        print(len(self.items))
        
    
    
    # top items in the stack
    def top(self):
        print(self.items[len(self.items)-1])

        
    # check stack is empty
    def check(self):
        if len(self.items)==0:
            print("Empty")
        else:
            print("Not empty")

n = Stack()
# n.push(3)
# n.push(4)
# n.push(5)
# n.push(9)
# n.pop(0)
# print(n)
# n.view()
# n.size()
# n.top()
# n.check()



        
while True:
    print("1. Push Item")
    print("2. Pop Item")
    print("3. Print Items in the stack")
    print("4. Size of the stack")
    print("5. Top item in the stack")
    print("6. Check stack is empty")
    
            
    choice = int(input("Enter your choice: ").strip())
    
    if choice == 1:
        n.push(input("Enter the item to add: "))
    
    elif choice == 2:
        n.pop(input("Enter the item to be removed: "))
        
    elif choice == 3:
        n.view() 
        
    elif choice == 4:
        n.size()
         
    elif choice == 5:
         n.top()
         
    elif choice == 6:
         n.check()
         
    exit()
    
else:
    print("Invalid choice")