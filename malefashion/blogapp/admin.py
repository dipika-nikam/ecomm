from django.contrib import admin
from .models import Blogs, Postcomments,Fav_blogs,PostImage,IP,Blogger_Profile

# Register your models here.
admin.site.register(Blogs),
admin.site.register(Postcomments),
admin.site.register(Fav_blogs),
admin.site.register(IP),
admin.site.register(Blogger_Profile),

class PostImageAdmin(admin.StackedInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Blogs

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
