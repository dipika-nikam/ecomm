from django import views
from django.urls import path
from . import views

urlpatterns = [
   path('',views.blogs_index,name='blog'),
   path('blog_create/',views.blog_create,name='blog_create'),
   path('my_blog/',views.my_blog,name='my_blog'),
   path('admin_approval', views.admin_approval, name='admin_approve'),
   path('<int:id>/details', views.blog_details, name='details'),
   path('<int:id>/blog_del', views.blog_del, name='blog_del'),
   path('fav_blogs',views.favblogs,name='fav_blogs'),
   path('<int:id>/add_fev_blog',views.add_fev_blog,name='add_fev_blog'),
   path('<int:id>/remove_fav',views.remove_fav,name='remove_fav'),
   # path('<int:id>/detail_view',views.detail_view,name='detail_view'),
]
