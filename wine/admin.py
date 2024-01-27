
from django.contrib import admin
from .models import MenuModel
# from django.utils.html import format_html

# Register your models here.

admin.site.register(MenuModel)


# @admin.register(MenuModel)
# class MenuAdmin(admin.ModelAdmin):
#     def image_tag(self, obj):
#         return format_html('<img src="/media/{obj.image}">')
    
#     image_tag.short_description = 'Image'

#     list_display = ['menu', 'body', 'price', 'image_tag',]
#     list_filter = ['menu']
#     ordering = ['menu']