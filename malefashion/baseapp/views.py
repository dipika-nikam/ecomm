from django.forms import model_to_dict
from django.shortcuts import redirect, render
from saler_app.models import Add_product
from blogapp.models import Blogs
from auths.models import NewUser
from .models import Cart, Wishlist
from django.conf import settings
from django.core.mail import send_mail
import random
from django.db.models import Q


# Create your views here.


def index(request):
    data = Add_product.objects.all()
    blog = Blogs.objects.all()
    context = {
        'data': data,
        'blog': random.choices(blog, k=3),
    }

    return render(request, 'index.html', context)


def shop(request):
    if 'search' in request.GET:
        search = request.GET.get('search')
        multiple_q = Q(Q(name__icontains=search))
        data = Add_product.objects.filter(multiple_q)

    elif 'start' in request.GET and 'end' in request.GET:
        start = request.GET.get('start')
        end = request.GET.get('end')
        data = Add_product.objects.filter(price__range=(start, end))
    else:
        data= Add_product.objects.all()
    return render(request, 'shop.html',{'data':data})


def cart(request):
    li = []
    data = Cart.objects.filter(user=request.user.id)
    total_item = len(data)
    for i in data.values():
        li.append(i['total'])

    return render(request, 'cart.html', {'data': data, 'all_total': sum(li), 'total_item': len(data)})

def add_cart(request,id):
    product=Add_product.objects.get(id=id)
    user = NewUser.objects.get(pk=request.user.id)
    cart = Cart.objects.create(user=user, product=product,quantity=1, total=product.price)
    return redirect('cart')

def del_cart(request, id):
    data = Cart.objects.filter(id=id)
    data.delete()
    return redirect('cart')

def wishlist(request):
    data = Wishlist.objects.all()
    return render(request, 'wish.html', {'data': data})


def add_wishlist(request, id):
    product = Add_product.objects.get(id=id)
    user = NewUser.objects.get(pk=request.user.id)
    add = Wishlist.objects.create(user=user, product=product)
    return redirect('wish')


def remove_wish(request, id):
    data = Wishlist.objects.get(id=id)
    data.delete()
    return redirect('wish')

def contact(request):

    if 'F_name' in request.GET and 'email' in request.GET and 'message' in request.GET:
        F_name = request.GET.get('F_name')
        email = request.GET.get('email')
        message = request.GET.get('message')

        subject = f'hello {F_name}'
        message = f'Hii {email}, Thank you for contacting {message}.'
        email_from = settings.EMAIL_HOST_USER
        recipient = [email]
        send_mail(subject, message, email_from, recipient)
        return redirect('contact')

    return render(request, 'contact.html')


