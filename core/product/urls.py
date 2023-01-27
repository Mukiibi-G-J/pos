from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #? products
    path('product-list', views.ProductList.as_view(), name='product_list'),
    path('add-product', views.addproduct, name='add_product'),
    path('upload_products', views.upload_products, name='upload_products'),
    path('list-category', views.list_category, name='list_category'),
    path('add_product_upload', views.add_product_upload, name='add_product_upload'),
    
    path('add-category', views.AddCategory, name='add_category'),
    path('add-sales', views.AddSale.as_view(), name='add_sales'),
    path('list_sales', views.ListSale.as_view(), name='list_sales'),
    path('add_purchases', views.AddPurchase.as_view(), name='add_purchases'),
    path('list_purchases', views.ListPurchase.as_view(), name='list_purchases')
]