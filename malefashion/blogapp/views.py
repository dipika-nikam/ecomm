from django.shortcuts import render, redirect
from .models import Blogs,Postcomments,Fav_blogs,PostImage,IP,Blogger_Profile
from .form import Blogforms
from auths.models import NewUser
from django.contrib import messages
from django.forms.models import model_to_dict
from django.db.models import Q

# Create your views here.

def blogs_index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        if search == 'not_approved':
            data = Blogs.objects.filter(is_approved=False)
        elif search == 'approved':
            data = Blogs.objects.filter(is_approved=True)
        else:
            data = Blogs.objects.filter(title__icontains=search,is_approved=True)
        # data = Blogs.objects.filter(title__icontains=search)

    elif 'start' in request.GET and 'end' in request.GET:
        start = request.GET.get('start')
        end = request.GET.get('end')
        data = Blogs.objects.filter(price__range=(start, end))
    else:
        data = Blogs.objects.all()
    li_img=[]
    new_data=Fav_blogs.objects.filter(user=request.user.id)
    for i in new_data:
        if i.blog in data:
            li_img.append(i.blog)

    return render(request, 'blog.html', {'data': data, 'fav_blogs': li_img})


def blog_create(request):
    form = Blogforms
    user = request.user
    if request.method == 'POST':
        form = Blogforms(request.POST, request.FILES)
        user = request.user
        user = NewUser.objects.get(pk=request.user.id)

        if form.is_valid():
            img = form.cleaned_data.get('image')
            form = form.save(commit=False)
            form.image = img
            form.user = user
            form.save()
            return redirect('index')
    return render(request, 'blog-create.html', {'form': form})


def my_blog(request):
    data = Blogs.objects.filter(user=request.user.id)
    context = {
        'data': data
    }
    return render(request, 'my-blog.html', context)


def admin_approval(request):
    blog_list = Blogs.objects.all()
    if request.user.is_superuser:
        if request.method == 'POST':
            blog_list.update(is_approved=False)
            id_list = request.POST.getlist('boxes')
            for i in id_list:
                Blogs.objects.filter(id=i).update(is_approved=True)
            messages.info(request, ('Admin Request Approved'))
            return redirect('admin_approve')
        else:
            context = {
                'blog_list': blog_list,
            }
            return render(request, 'admin_panel.html', context)
    else:
        messages.success(request, ('You are not authorized to view this page'))
    return render(request, 'admin_panel.html')

def blog_details(request,id):
    data = Blogs.objects.get(id=id)
    photos = PostImage.objects.filter(post=data)
    # user = NewUser.objects.get(id=request.user.id)
    if 'name' in request.GET and 'comment' in request.GET:
        name = request.GET['name']
        comments = request.GET['comment']
        Postcomments.objects.create( user=request.user, blog=data,name=name, Comment=comments)

    if request.user == data.user:
        commen = Postcomments.objects.filter(blog=data)
        if request.method=='POST' :
            approve_id = request.POST.get('boxes')
            Postcomments.objects.filter(id=approve_id).update(is_approved=True)

    def get_ip(request):
        address= request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip=request.META.get('REMOTE_ADDR')
            return f'{ip}'
    ip =get_ip(request)
    user = NewUser.objects.get(id=request.user.id)
    u = IP(ip=ip,user=user,blog=data)
    multiple_q = Q(Q(ip__icontains=ip,user=user,blog=data))
    result = IP.objects.filter(multiple_q)
    if len(result) >= 1:
        print('user exist')
    else:
        u.save()
        count = IP.objects.filter(blog=data).count()
        data.count = count
        data.save()
    commen = Postcomments.objects.filter(blog=data)
    contex={
        'blog_list': data,
        'comments': commen,
        'photos' : photos,
    }
    return render(request, 'blog_details.html',contex)

def blog_del(request,id):
    data = Blogs.objects.filter(id=id)
    data.delete()
    return redirect('blog')

def favblogs(request):
    data = Fav_blogs.objects.filter(user=request.user.id)
    return render(request, 'fev.html', {'data': data})

def add_fev_blog(request, id):
    blog = Blogs.objects.get(id=id)
    user = NewUser.objects.get(pk=request.user.id)
    msg = messages.success(request,"Successfull add blog as fav.")
    Fav_blogs.objects.create(user=user, blog=blog)

    return redirect('fav_blogs')

def remove_fav(request, id):
    data = Fav_blogs.objects.get(id=id)
    data.delete()
    return redirect('fav_blogs')

def profile_view(request,id):
    get_blog = Blogs.objects.get(id=id)
    profile = Blogger_Profile.objects.get(user=get_blog.user)
    my_blogs = Blogs.objects.filter(profile=profile).order_by('-count')
    print(profile)
    context = {
        'data': profile,
        'blog': my_blogs,
    }
    return render(request, 'profile.html',context)

