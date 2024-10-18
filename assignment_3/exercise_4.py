# class the items characteristcs: barcode, name,price
# while loop input receipt y/n
# while yes == True input new item barcode + input quantity
#   after input add onther item
# loop untill elif is no stop looping
# else system exit return false 
# when no output/print(itemName, quantity, total price )(quantity*price )

class Item:
    def __init__(self,barcode,name,price):
        self.barcode=barcode
        self.name=name
        self.price=price

class Receipt:
    def __init__(self):
        self.items = []
        self.total_quantity = 0
        self.total_cost = 0
        
    def add_item(self,item,quantity):
        self.items.append((item,quantity))
        self.total_quantity += quantity
        self.total_cost += item.price*quantity
        
    def print_receipt(self):
        print("Receipt")
        print("----------------")
        for item, quantity in self.items:
            print(f"{item.name}({quantity}):{item.price*quantity:.2f}")
            print("---------------")
            print(f"Total:{self.total_cost:.2f}")
            
def main():
    items = [
        Item(1,"Apple",0.5),
        Item(2,"Banana",0.75),
        Item(3,"Orange",0.6)
    ]
    
    while True:
        receipt = Receipt()
        print("Do you want to start an new receipt?(yes/no):")
        if input().lower != "yes":
            break
    while True:
        print("Enter item barcode(or 'quit' to finish):")
        barcode=input()
        if barcode == "quit":
            break
        
        item = next((item for item in items if item.barcode == barcode),None)
        if item is None:
            print("Invalid barcode. Please try again.")
            continue
        elif barcode == item:
            print("Enter quantity:")
        quantity=int(input())
        receipt.add_item(item,quantity)
        print("Do you want to add another item?(yes/no):")
        if input().lower() != "yes":
            break
    receipt.print_receipt()
if __name__ == "__main__":
    main()