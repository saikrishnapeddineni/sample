class product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_saved=price-deal_price
    def display_order_details(self):
        print("product:{}".format(self.name))
        print("price:{}".format(self.price))
        print("deal_price:{}".format(self.deal_price))
        print("ratings:{}".format(self.ratings))
        print("you_saved:{}".format(self.you_saved))
    def get_deal_price(self):
        return self.deal_price
class ElectronicItem(product):
    def display_order_details(self):
        super().display_order_details()#methodoverriding
        print(self.warranty_in_months)
    def set_warranty(self,warranty_in_months):

        self.warranty_in_months=warranty_in_months
class order:
    def __init__(self,delivery_speed,delivery_adress):
        self.items_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_adress=delivery_adress
    def add_item(self,product,quantity):
        self.items_cart.append((product, quantity))
    def display_order_details(self):
        for product,quantity in self.items_cart:
            product.display_order_details()
            print("quantity:{}".format(quantity))
    def display_total_bill(self):
        for product, quantity in self.items_cart:
            price=product.deal_price*quantity
            print(price)


tv=ElectronicItem('Tv',35000,28000,3.5)
tv.set_warranty(6)
ord=order('prime','ulavapadu')
ord.add_item(tv,5)
ord.display_order_details()
ord.display_total_bill()
