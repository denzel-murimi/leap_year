class Classey:
    varia=2

    def method(self):
        print(self.varia)

object_1=Classey()
object_2=Classey()

object_1.varia=3
object_2.varia=5

#print(object_1.varia)

class Transport:
    def __init__(self, air, water):
        self.air=air
        self.water=water

#obj_transport=Transport("Beluga", "Hovercraft")
#print(obj_transport.air,obj_transport.water)

class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname,self.lname)

#x=Person("John", "Doe")
#x.printname()

class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self,item_name,quantity):
        item=(item_name,quantity)
        self.items.append(item)

    def remove_item(self,item_name):
        for item in self.items:
            if item[0]== item_name:
                self.items.remove(item)
                break
 #this method is calculating the total items in our list
    def calculate_total(self):
        total=0
        for item in self.items:
            total += int(item[1])
        return total

cart=ShoppingCart()
cart.add_item("Kiwi","5")
cart.add_item("Papaya","4")
cart.add_item("Mangoes","14")

print("Current items in cart:")
for item in cart.items:
    print(item[0], "-", item[1])
total_qty=cart.calculate_total()
print("Total Quantity: ", total_qty)