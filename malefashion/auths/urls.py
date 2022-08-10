from django.urls import path, include
from . import views

urlpatterns = [
    path('register',views.register, name='register'),
    path('login',views.signin, name='login'),
    path('logout',views.user_logout, name='logout'),

]
