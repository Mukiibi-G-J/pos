from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('product-list', views.ProductList.as_view(), name='product_list'),
    path('add-product', views.AddProduct.as_view(), name='add_product'),
    path('list-category', views.ListCategory.as_view(), name='list_category'),
    # path('add-category', views.AddCategory.as_view(), name='add_category'),
    path('add-category', views.AddCategory, name='add_category'),
    path('add-sales', views.AddSale.as_view(), name='add_sales'),
    path('list_sales', views.ListSale.as_view(), name='list_sales'),
    path('add_purchases', views.AddPurchase.as_view(), name='add_purchases'),
    path('list_purchases', views.ListPurchase.as_view(), name='list_purchases')
]