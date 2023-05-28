from django.contrib import admin
from . models import *

from .models import Category, Product, ProductImage, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','slug','description','price','old_price','is_featured', 'num_available','last_visit')
    search_fields = ('title','slug','price','old_price','is_featured', 'num_available','last_visit')

    def set_price_to_one(self,request,queryset):
        queryset.update(price=1)

    actions =('set_price_to_one',)
    list_editable = ('price','slug','description','is_featured')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReview)