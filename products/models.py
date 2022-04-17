from curses import meta
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models  import User
from django.utils import timezone
from django.contrib.auth.models import User

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.brand_name
class Product_Unit(models.Model):
  
    unit_name = models.CharField(max_length=25)
    def __str__(self):
        return self.unit_name
    
class Category(models.Model):
   
    category_name = models.CharField(max_length=255, null=False, blank=False ,unique=True)
    category_image = models.ImageField(null=True,  default='images/default.png', upload_to='images/')
    class Meta:
        db_table='Category'
        verbose_name="Category"
        verbose_name_plural='Categories'

    def __str__(self):
        return self.category_name
class Products(models.Model):
    unit_name=(
        ("pcs","PCS",),
       ("dozen","DOZEN",),
     )
    product_code = models.CharField(max_length=55,blank=False, null=False)
    # prouct_imgae = models.ImageField()
    product_name = models.CharField(max_length=255, blank=False, null=False)
    unit_id = models.CharField(max_length=255, choices=unit_name)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_in_stock = models.IntegerField(default=0, null=True)
    unit_price = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    reorder_level = models.IntegerField(default=0, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
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
        
        
        
class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural ='Orders'
        db_table= 'Orders'
        # ordering= ('-publish',)
    
    
    def __str__(self):
        return f"{self.product} ordered by {self.staff}"
    