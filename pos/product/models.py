
from django.db import models
from django.contrib.auth.models  import User
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError

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
    product_code = models.CharField(max_length=55,blank=False, null=False, unique=True)
    # prouct_imgae = models.ImageField()
    product_name = models.CharField(max_length=255, blank=False, null=False)
    description  = models.TextField(max_length=255, blank=False, null=False)
    unit_id = models.CharField(max_length=255, choices=unit_name)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField(default=0, null=True)
    unit_price = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    reorder_level = models.IntegerField(default=0, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    export_csv = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    
    def clean(self):
        if self.quantity_in_stock is not None and self.quantity_in_stock < 0:
            raise ValidationError('Quantity in stock must be a positive number.')
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
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
    
    
# class Sale(models.Model):
   
#     total_price = models.IntegerField()
#     # payment_method = models.CharField(max_length=50)
#     # is_complete = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['-timestamp']

class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    total = models.IntegerField()
    stock_left = models.IntegerField()
    
    
    
    def __str__(self):
         
         return f"{self.product} sold by {self.user}"
        
        
    # @property    
    # def total_sales_of_today(self):
    #     sales = Sales.objects.filter(timestamp__date=datetime.date.today())        
    #     return sum(sale.total for sale in sales)
    # @property
    # def get_current_product_stock(self):
    #     return self.product.quantity_in_stock
    

    class Meta:
        ordering = ['-timestamp']
        
    def save(self, *args, **kwargs):
        if self.product.quantity_in_stock < self.quantity:
            raise Exception('Not enough stock')
        else:
            print(kwargs)
            self.product.quantity_in_stock = self.product.quantity_in_stock - kwargs.get('quantity', self.quantity)
            self.stock_left = self.product.quantity_in_stock
            self.product.save()
            
        super(Sales, self).save(*args, **kwargs)