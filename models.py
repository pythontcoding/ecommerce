from django.db import models

# Create your models here.

class SliderManager(models.Model):
    title=models.CharField(max_length=225)
    image=models.ImageField(upload_to='slider_images')
    status=models.BooleanField(default=True)

    class Meta:
        db_table="slider_manager"





class ProductCategory(models.Model):

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='category')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=30)
    slug=models.CharField(max_length=30)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,null=True)
    description=models.TextField()
    regular_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    special_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    stocks=models.IntegerField(default=0)
    status=models.BooleanField(default=1)
    is_offer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    modifed_at = models.DateTimeField(auto_now=True)






class ProductImages(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image_name=models.ImageField(upload_to='products')
    is_default=models.BooleanField(default=0)



