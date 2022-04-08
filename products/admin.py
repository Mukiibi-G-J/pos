from django.contrib import admin
from . import models


@admin.register( models.Products)
class ModleAdmin(admin.ModelAdmin):
    list_display = ('product_code', 'product_name',
                    'unit_price', 'cost', 'reorder_level')
    search_fields = ('product_code', 'product_name')
    order_by = ('created_at')


admin.site.site_header = "Semuna POS"
    


admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.Product_Unit)


