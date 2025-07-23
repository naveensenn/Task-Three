class inventory:
    def __init__(self):
        self.inventory = {}
        
    def addInventory(self,product_name,product_quantity,product_price):
        self.inventory[product_name]={"product_quantity":product_quantity,"product_price":product_price}
        print(f"Product {product_name} added to inventory.")
        
        
    def updateQuantity(self,product_name,product_quantity):
        if product_name in self.inventory:
            self.inventory[product_name]["product_quantity"]=product_quantity
            print(f"Quantity {product_quantity}  updated for product {product_name}.")
            
    def updatePrice(self,product_name,product_price):
        if product_name in self.inventory:
            self.inventory[product_name]["product_price"]=product_price
            print(f"Price {product_price} updated for product {product_name}.")
    
    def removeInventory(self,product_name):
        if product_name in self.inventory:
            del self.inventory[product_name]
            print(f"Product {product_name} removed from inventory.")
            
            
        
    def showInventory(self):
        for name,info in self.inventory.items():
            print(f"Product: {name}, Quantity: {info['product_price']},Price: {info['product_price']}")
                

shop = inventory()

# shop.addInventory("Cloth",400,800)
shop.addInventory("Shoes",100,1000)

shop.updateQuantity("Shoes",900)

shop.addInventory("Food","200","400")


shop.showInventory()