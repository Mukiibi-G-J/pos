from django.contrib import admin
from . import models
admin.site.site_header = "Semuna POS"


   # <------decorater------------>
@admin.register( models.Products)
class ModleAdmin(admin.ModelAdmin):
    list_display = ('product_code', 'product_name',
                    'unit_price', 'cost', 'reorder_level')
    search_fields = ('product_code', 'product_name')
    order_by = ('created_at')



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_image','category_id','category_name']
    



admin.site.register(models.Brand)
admin.site.register(models.Product_Unit)


