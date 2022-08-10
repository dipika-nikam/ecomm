from django.db import models
from auths.models import NewUser

# Create your models here.
category = (
    ('Shoes', 'Shoes'),
    ('Jacket', 'Jacket'),
    ('Shirt', 'Shirt'),
    ('T-shirt', 'T-shirt'),
    ('Bag', 'Bag'),
    ('Glasses', 'Glasses'),
    ('Others', 'Others'),
)

class Add_product(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to= 'products/images/')
    price= models.IntegerField()
    category = models.CharField(max_length=20, choices=category)

    def __str__(self):
        return self.name



