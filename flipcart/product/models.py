from django.db import models

from .category import Category


class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    desc=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/laptop.jpg')

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_category(get_id):
        if get_id:
            return Product.objects.filter(category=get_id)
# models
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def isexists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
    @staticmethod
    def get_email(email):

        try:

            return Customer.objects.get(email=email)
        except:
            return False


