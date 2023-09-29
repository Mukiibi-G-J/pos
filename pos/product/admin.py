from django.contrib import admin
from . import models
from django.shortcuts import render
from django.urls import path, reverse
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from mptt.admin import MPTTModelAdmin

admin.site.site_header = "Semuna POS"


# <------decorater------------>
@admin.register(models.Products)
class ModleAdmin(admin.ModelAdmin):
    list_display = (
        "product_code",
        "product_name",
        "unit_price",
        "quantity_in_stock",
        "cost",
        "reorder_level",
        "new_arrival",
    )
    search_fields = ("product_code", "product_name")
    order_by = "created_at"


admin.site.register(models.Brand)
admin.site.register(models.Product_Unit)


# csv upload form
class CategoryAdminCSV(forms.Form):
    csv_upload = forms.FileField()


@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ["category_name", "category_image"]

    def upload_csv(self, request):
        form = CategoryAdminCSV()

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith(".csv"):
                messages.waring(request, "the wrong file type was upload")
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            # >>['category_name, 01', 'Bags, 01', 'Bottles, 01', 'Bowls, 01', 'Busengeja, 01', 'Dish, 01', 'Flaskcup, 01', 'Flasks, 01', 'Flying pans, 01', 'Food Flasks, 01']
            print(csv_data)
            for x in csv_data:
                fields = x.split(",")
                created = models.Category.objects.update_or_create(
                    category_name=fields[0]
                )
            url = reverse("admin:index")
            return HttpResponseRedirect(url)
        context = {"form": form}
        return render(request, "admin/csv_upload.html", context)

    # registeting  a a url  to admin site
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv/", self.upload_csv)]
        return new_urls + urls


@admin.register(models.Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "purchase_price",
        "purchase_date",
        "supplier",
        "created_at",
    )
    search_fields = ("product", "supplier")


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "price",
        "date_sold",
    )
    search_fields = ("product",)
    list_filter = ("date_sold",)
