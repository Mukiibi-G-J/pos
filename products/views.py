from .form import CategoryForm
from django.shortcuts import render
from django.views import generic
# Create your views here.


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

class AddProduct(generic.TemplateView):
    template_name = 'products/add_products.html'

class ProductList(generic.TemplateView):
    template_name = 'products/prod_list.html'

class ListCategory(generic.TemplateView):
    template_name = 'categories/list_cat.html'
    
# class? AddCategory(generic.TemplateView):
    
#     template_name = 'categories/add_cat.html'
#    
def AddCategory(request):
    error=None
    if request.method == "POST":
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            error ='something went wrong'

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