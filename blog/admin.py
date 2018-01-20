from django.contrib import admin

from .models import Post,Category,Tag

# Register your models here. 管理Django后台的界面修改

class PostAdmin(admin.ModelAdmin): #在Django管理后台页面增加详细的信息
    list_display = ['title','create_time','modified_time','category','author']



admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
