# class Classey:
#     varia=2
#
#     def method(self):
#         print(self.varia)
#
# object_1=Classey()
# object_2=Classey()
#
# object_1.varia=3
# object_2.varia=5
#
# #print(object_1.varia)
#
# class Transport:
#     def __init__(self, air, water):
#         self.air=air
#         self.water=water
#
# #obj_transport=Transport("Beluga", "Hovercraft")
# #print(obj_transport.air,obj_transport.water)
#
# class Person:
#     def __init__(self, fname, lname):
#         self.fname=fname
#         self.lname=lname
#
#     def printname(self):
#         print(self.fname,self.lname)
#
# #x=Person("John", "Doe")
# #x.printname()

class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self,item_name:str,quantity:float,unit_price:float):
        item=(item_name,quantity,unit_price)
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

    def calculate_price(self)->float:
        total=0.00
        for item in self.items:
            total+= int(item[1])*int(item[2])
        return total
    def cart_contents(self):
        print("Items in cart:")
        for item in self.items:
            print(item[0], "-", item[1],"@",item[2], "each")
        print(f"Total: Ksh {self.calculate_price():.2f}\n")

# cart=ShoppingCart()
# cart.add_item("Kiwi","10","100")
# cart.add_item("Papaya","10","100")
# cart.add_item("Mangoes","10","100")
#
# print("Current items in cart:")
# for item in cart.items:
#     print(item[0], "-", item[1],"@",item[2], "each")
# total_qty=cart.calculate_price()
# print("Total Price: ", total_qty)

class DiscountedCart(ShoppingCart):
    def __init__(self,discount_rate:float):
        super().__init__()
        self.discount_rate=discount_rate
    def calculate_price(self)->float:
        initial_price=super().calculate_price()
        discount=initial_price*self.discount_rate
        return initial_price-discount

class TaxedCart(ShoppingCart):
    def __init__(self,tax_rate:float):
        super().__init__()
        self.tax_rate=tax_rate
    def calculate_price(self)->float:
        initial_price=super().calculate_price()
        tax=initial_price*self.tax_rate
        return initial_price+tax
class FinalCart(ShoppingCart):
    def __init__(self,discount_rate:float,tax_rate:float):
        super().__init__()
        self.discount_rate=discount_rate
        self.tax_rate=tax_rate
    def calculate_price(self) ->float:
        initial_price=super().calculate_price()
        discount=initial_price*self.discount_rate
        discounted_total=initial_price-discount
        tax=discounted_total*self.tax_rate
        return discounted_total+tax

def checkout(cart:ShoppingCart):
    cart.cart_contents()
    print(f"Total amount is: Ksh {cart.calculate_price():.2f}\n")

if __name__=="__main__":
    obj_cart=ShoppingCart()
    obj_cart.add_item("Kiwi",50,35)
    obj_cart.add_item("Papaya",30,50.56)
    obj_cart.add_item("Mangoes",35,20.67)
    print(">>Ordinary cart without tax & discount<<")
    checkout(obj_cart)

    disc_obj=DiscountedCart(discount_rate=0.10)
    disc_obj.add_item("Kiwi",50,35)
    disc_obj.add_item("Papaya",30,50.56)
    disc_obj.add_item("Mangoes",35,20.67)
    print(">>Cart after 10% Discount<<")
    checkout(disc_obj)

    tax_obj=TaxedCart(tax_rate=0.16)
    tax_obj.add_item("Kiwi",50,35)
    tax_obj.add_item("Papaya",30,50.56)
    tax_obj.add_item("Mangoes",35,20.67)
    print(">>Cart after 16% Tax<<")
    checkout(tax_obj)


    final_obj=FinalCart(0.10,0.16)
    final_obj.add_item("Kiwi",50,35)
    final_obj.add_item("Papaya",30,50.56)
    final_obj.add_item("Mangoes",35,20.67)
    print(">>Cart after Tax and Discount<<")
    checkout(final_obj)







