from curses import meta
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models  import User
from django.utils import timezone

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.brand_name
class Product_Unit(models.Model):
  
    unit_name = models.CharField(max_length=25)
    def __str__(self):
        return self.unit_name
    
class Category(models.Model):
    catergory_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.catergory_name
class Products(models.Model):
    product_code = models.CharField(max_length=55,blank=False, null=False)
    # prouct_imgae = models.ImageField()
    product_name = models.CharField(max_length=255, blank=False, null=False)
    unit_id = models.ForeignKey(Product_Unit, on_delete=models.CASCADE)
    catergory_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_in_stock = models.IntegerField(default=0, null=True)
    unit_price = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    reorder_level = models.IntegerField(default=0, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    export_csv = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural ='Products'
        db_table= 'Products'
        ordering= ('-publish',)
        
    def __Str__(self):
        return self.product_name
        