from django.contrib import admin
from .models import Product, Category, Size, ProductImage

class AdminInlineSize(admin.TabularInline):
    extra = 1
    model = Size

class AdminInlineProductImage(admin.TabularInline):
    extra = 1
    model = ProductImage

class AdminCategory(admin.ModelAdmin):

    def image(obj):
        return "<img src='%s' width='200'>" % (obj.image.url)
    image.allow_tags = True

    list_display = ('name','slug', image)

class AdminProduct(admin.ModelAdmin):

    def image(obj):
        return "<img src='%s' width='100'>" % (obj.main_image.url)
    image.allow_tags = True

    list_display = ('name', 'category', 'price', 'is_active', image)
    inlines = [AdminInlineSize,AdminInlineProductImage]

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
