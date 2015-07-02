from django.contrib import admin
from .models import Product, Category, Option, ProductImage

class AdminInlineSize(admin.TabularInline):
    extra = 1
    model = Option

class AdminInlineProductImage(admin.TabularInline):
    extra = 1
    model = ProductImage

class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)

class AdminProduct(admin.ModelAdmin):

    def image(obj):
        return "<img src='%s' width='100'>" % (obj.main_image.url)
    image.allow_tags = True

    list_display = ('name', 'category', 'price', 'is_active', image)
    inlines = [AdminInlineSize,AdminInlineProductImage]

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
