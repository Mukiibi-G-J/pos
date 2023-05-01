from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode


app_name = "products"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # ? products
    path("product-list", views.ProductList.as_view(), name="product_list"),
    path("add-product", views.addproduct, name="add_product"),
    path("add_single_product", views.add_single_product, name="add_single_product"),
    path("upload_products", views.upload_products, name="upload_products"),
    path("list-category", views.list_category, name="list_category"),
    path("add_product_upload", views.add_product_upload, name="add_product_upload"),
    path("add-category", views.AddCategory, name="add_category"),
    # sales
    path("add_sales", views.AddSale.as_view(), name="add_sales"),
    path("list_sales", views.ListSale.as_view(), name="list_sales"),
    path("product_search", views.AddSale.as_view(), name="product_search"),
    path("complete_sale", csrf_exempt(views.complete_sale), name="complete_sale"),
    #! purchases
    path("add_purchases", views.AddPurchase.as_view(), name="add_purchases"),
    path("list_purchases", views.ListPurchase.as_view(), name="list_purchases"),
    path(
        "generate_purchase_list",
        views.generate_purchase_list,
        name="generate_purchase_list",
    ),
    path("add_single_sell", views.add_single_sell, name="add_single_sell"),
    path("upload_purchase", views.upload_purchase, name="upload_purchase"),
    #!report
    path("reports", views.reports, name="reports"),
    # utils
    path("generate_barcode", views.generate_barcode, name="generate_barcode"),
    path(
        "get_product_by_uuid/<str:uuid>",
        views.get_product_by_uuid,
        name="get_product_by_uuid",
    ),
    # export to excel
    path("export_to_excel", views.export_to_excel, name="export_to_excel"),
]
