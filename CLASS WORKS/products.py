class sportMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}
        
    def createOrder(self,Orderid,ItemName,Quantity,Price,Total):
        temp = {
            "orderid": Orderid,
            "itemname": ItemName,
            "quantity": Quantity,
            "price": Price,
            "total": Total
        }
        
        self.orders[Orderid] = temp
        
    def createInventory(self,ProductID,ProductName,Quantity,Price):
        temp = {
            "productid": ProductID,
            "productname": ProductName,
            "quantity": Quantity,
            "price": Price
        }
        
        self.inventory[ProductID] = temp
        
    def printOrders(self):
        print(self.orders)
       
        
    def printInventory(self):
        print(self.inventory)
        
    def updateInventory(self):
        print(self.inventory)
        

trinity = sportMart()


orders = open("orders.csv","r")
orders_header = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(',')
    trinity.createOrder(temp[0],temp[1],temp[2],temp[3],temp[4])
    
    trinity.printOrders()
    
    
inventory = open("inventory.csv","r")
inventory_header = inventory.readline()
inventory_inventory = inventory.readlines()
for item in inventory_inventory:
    temp = item.strip().split(',')
    trinity.createInventory(temp[0],temp[1],temp[2],temp[3])
    
    trinity.printInventory()
    
# create a menu driven program that will 
# --> create new orders and update the inventory accordingly
# --> export the final data to the file    

while True:
    print("Menu Options")
    print("1. Create new orders")
    print("2. Update Inventory")
    print("3. Exit")
    
    choice = input("Enter the choice").strip()
    if choice == "1":
        
    elif choice == "2":
        
    elif choice == "3":
        exit()
    else:
        print("Invalid Choice")