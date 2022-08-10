from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('shoppping',views.shop,name='shop'),
    path('mycart',views.cart,name='cart'),
    path('<int:id>/newcart',views.add_cart , name='add_cart'),
    path('<int:id>/delete_cart',views.del_cart , name='delete_cart'),
    path('wish/', views.wishlist, name='wish'),
    path('<int:id>/add_wishlist/', views.add_wishlist, name='add_wishlist'),
    path('<int:id>/remove_wish/', views.remove_wish, name='remove_wish'),
    path ('contact/', views.contact, name='contact'),

]
