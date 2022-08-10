import email
from django.db import models
from auths.models import NewUser
from  ckeditor.fields import RichTextField

# Create your models here.
class Blogger_Profile(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to = 'Blogger_Profile')
    profession = models.CharField(max_length=255)
    github = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255)

    def __str__(self):
        return self.name
class Blogs(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    profile =models.ForeignKey(Blogger_Profile,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='Blogs')
    images = models.FileField(blank=True)
    # descripation = models.CharField(max_length=1550)
    descripation = RichTextField(blank=True, null= True)
    is_approved = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

    def __str__(self):
        return  self.title


class PostImage(models.Model):
    post = models.ForeignKey(Blogs, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title


class Postcomments(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    Comment = models. TextField()
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Fav_blogs(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog

class IP(models.Model):
    ip= models.CharField(max_length=40)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    blog= models.ForeignKey(Blogs, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip


