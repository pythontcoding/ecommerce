from django.contrib import admin
from products.models import Product,ProductImages, ProductCategory,SliderManager

# Register your models here.

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 0
    min_num=1
    max_num = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'regular_price', 'special_price', 'stocks')
    list_filter = ('status','stocks')

    inlines=[ProductImagesInline]


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_at')




    


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(SliderManager)