# create a aclass restaurant, that accepts
# itemname and quantity as input
# inside your class you are having the item
# and its cost(unit price) as a dictionary
# create a function calculate totalcost
# that prints the itemname, qty & totalcost


class restaurant:
    
    def __init__(self,itemname,qty):
        self.itemname = itemname
        self.qty = qty
        self.menuItems = {
            "RICE": 30,
            "CHICKEN": 100,
            "DAL": 40,
            "CHAPATHI": 15,
            
        }
        
    def totalCost(self):
        print("Item\t: ",self.itemname)
        print("Quantity\t: ",self.qty)
        total = self.qty * self.menuItems[self.itemname]
        print("Total\t: ",total)
 
itemname = input("Item Name: ")
qty = int(input("Quantity: "))
 
            
order = restaurant(itemname,qty)
order.totalCost()
