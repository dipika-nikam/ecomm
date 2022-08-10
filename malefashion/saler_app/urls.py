from django.urls import path
from . import views

urlpatterns = [
    path('Add_product/', views.add_product,name='Add_product'),
]
