from django.db import models
from auths.models import NewUser
from saler_app.models import Add_product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Add_product, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    total= models.IntegerField()

    def __str__(self):
        return self.quantity

class Wishlist(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    product= models.ForeignKey(Add_product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product


