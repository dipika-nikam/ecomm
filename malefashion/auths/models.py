from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
usertype= (
    ('Saler Acoount', 'Saler Acoount'),
    ('Buyer Acoount', 'Buyer Acoount'),
)

class NewUser(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(max_length=255,choices=usertype, default= 'Buyer Acoount')

    def __str__(self):
       return self.username

