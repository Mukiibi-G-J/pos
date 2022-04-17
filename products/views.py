from .form import CategoryForm,AddProductForm
from django.shortcuts import render
from django.views import generic
from .models import Category


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

class AddProduct(generic.TemplateView):
    template_name = 'products/add_products.html'

class ProductList(generic.TemplateView):
    template_name = 'products/prod_list.html'

def addproduct(request):
    form =AddProductForm()
    context={
    'form':form
    }

    return render(request, 'products/add_products.html', context)


def list_category(request): 
    categories = Category.objects.all()
    context={
        'categories': categories
    }

    return render(request, 'categories/list_cat.html', context)
       
def AddCategory(request):
    error= None
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            error=form.errors
    else:
        form =CategoryForm()
    context={"form":form,
            "error":error  }
    return render(request, 'categories/add_cat.html', context )

class AddSale(generic.TemplateView):
    template_name = 'sales/add_sales.html'

class ListSale(generic.TemplateView):
    template_name = 'sales/list_sales.html'
    

class AddPurchase(generic.TemplateView):
    template_name = 'purchases/add_purchases.html'
    
class ListPurchase(generic.TemplateView):
    template_name = 'purchases/list_purchases.html'    