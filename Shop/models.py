from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category=models.CharField(max_length=50,default=" ")
    sub_category=models.CharField(max_length=50,default=" ")
    price=models.IntegerField(default=" ")
    desc=models.CharField(max_length=1000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="Shop/images",default=" ")

    category_choices = (
        ('Electronics', 'Electronics'),
        ('Clothes', 'Clothes')
    )
    sub_category_choice = (
        ('Electronics', 'Mobile'),
        ('Electronics', 'TV'),
        ('Clothes', 'Men s clothes'),
        ('Clothes', 'Women s clothes')
    )
    category = MultiSelectField(choices=category_choices)
    sub_category = MultiSelectField(choices=sub_category_choice)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default=" ")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=" ")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

