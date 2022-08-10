from django.shortcuts import redirect, render
from .models import Add_product
from .forms import Productsform
from auths.models import NewUser

# Create your views here.
def add_product(request):
    form = Productsform
    user= request.user
    if request.method == 'POST':
        form = Productsform(request.POST, request.FILES)
        user = request.user
        user = NewUser.objects.get(pk=request.user.id)

        if form.is_valid():
            img =form.cleaned_data.get('image')


            form= form.save(commit=False)
            form.image= img
            form.user= user
            form.save()
            return redirect('index')
    return render(request, 'seller/add_product.html', {'form': form})



