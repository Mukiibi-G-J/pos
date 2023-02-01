from product.form import CategoryForm,AddProductForm
from django.shortcuts import render
from django.views import generic
from product.models import *
from django.http import JsonResponse
from .form import FileUploadForm
import pandas as pd
# openpyxl
from openpyxl import load_workbook
import uuid
from barcode import Code128
from barcode.writer import ImageWriter
import uuid
from django.conf import settings
import os



def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

class AddProduct(generic.TemplateView):
    template_name = 'products/add_products.html'

class ProductList(generic.TemplateView):
    template_name = 'products/prod_list.html'

def addproduct(request):
    form =AddProductForm()
    uploadform = FileUploadForm()
    context={
    'form':form,
    'uploadform':uploadform
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
    
    
    


def upload_products(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            
            file = form.cleaned_data['file']
             # sheet
            wb = load_workbook(file)
            # get all sheet names
            sheets = wb.get_sheet_names()
            context = {
                "products":[]
            }
            for sheet in sheets:
                # get sheet by name
                ws = wb.get_sheet_by_name(sheet)
                values = [row[1:] for row in ws.values]
                # convert to dataframe
                
                df = pd.DataFrame(values)
                
                header_list = ['PRODUCT NAME' ,'DESCRIPTION', 'QUANTITY',  'PURCHASE PRICE',  'SALES PRICE' , 'CATEGORY' ,'UNIT ID' , 'BRAND']
                #check if header is in the first row
                
                if df.iloc[0].tolist() == header_list:
                    df = df[0:]
                    # get the first row as header
                    df.columns = df.iloc[0]
                    # drop the first row
                    df = df[1:]
                    # reset index
                    df = df.reset_index(drop=True)
                    # drop nonwe in PURCHASE PRICE, SALES PRICE, QUANTITY, PRODUCT NAME
                    df = df.dropna(subset=['PURCHASE PRICE', 'SALES PRICE', 'QUANTITY', 'PRODUCT NAME', 'CATEGORY', 'UNIT ID', 'BRAND'])
                    # get the first row as header
                    product_name = df['PRODUCT NAME'].tolist()
                    description = df['DESCRIPTION'].tolist()
                    quantity = df['QUANTITY'].tolist()
                    purchase_price = df['PURCHASE PRICE'].tolist()
                    sales_price = df['SALES PRICE'].tolist()
                    category = df['CATEGORY'].tolist()
                    unit = df['UNIT ID'].tolist()
                    brand = df['BRAND'].tolist()
                    
                  
                    for i in range(len(product_name)):
                        # create uuid
                        code = uuid.uuid4()
                        code = str(code).replace('-', '')[:14]
                        barcode = Code128(code, writer=ImageWriter())
                        print(code)
                        
                        # create context

                        products = {
                             'uuid':code,
                            'product_name':product_name[i],
                            'description':description[i],
                            'quantity':quantity[i],
                            'purchase_price':purchase_price[i],
                            'sales_price':sales_price[i],
                            'category':category[i],
                            'unit':unit[i],
                            'brand':brand[i]
                        }
                        
                        context['products'].append(products)
                    return render(request, 'products/add_products.html', context)
                        
                else:
                    print('header not found')
    return  render(request, 'products/add_products.html')


def add_product_upload(request):
    
    if request.method == 'POST':
        data = request.POST
        # get values form the dict
        for  i in request.POST.getlist('product_name'):  
            product_name = request.POST.getlist('product_name')
            description = request.POST.getlist('description')
            quantity = request.POST.getlist('quantity')
            purchase_price = request.POST.getlist('purchase_price')
            sales_price = request.POST.getlist('sales_price')
            category = request.POST.getlist('category')
            unit = request.POST.getlist('unit')
            brand = request.POST.getlist('brand')
            uuid = request.POST.getlist('uuid')
            # print(product_name, description, quantity, purchase_price, sales_price, category, unit, brand, uuid)
        for (product_name, description, quantity, purchase_price, sales_price, category, unit, brand, uuid) in zip(product_name, description, quantity, purchase_price, sales_price, category, unit, brand, uuid):
            print(product_name, description, quantity, purchase_price, sales_price, category, unit, brand, uuid)
            # delte all prod
            # Products.objects.all().delete()
            # Category.objects.all().delete()
            # Brand.objects.all().delete()
            if Category.objects.filter(category_name=category).exists() == False:
                category = Category.objects.create(category_name=category)
                category.save()
            else:
                category = Category.objects.get(category_name=category)
            
            if  Brand.objects.filter(brand_name=brand).exists() == False:
                brand = Brand.objects.create(brand_name=brand)
                brand.save()
            else:
                brand = Brand.objects.get(brand_name=brand)
                brand.save()
                
            products = Products.objects.create(
                product_name = product_name,
                description = description,
                unit_in_stock = quantity,
                unit_price = purchase_price,
                cost = sales_price,
                category_id = category,
                unit_id = "1",
                brand = brand,
                product_code = uuid
            )
            products.save()

                    
        return JsonResponse({'success':True})
    return JsonResponse({'success':False})        


def generate_barcode(request):
    product = Products.objects.all()
    for uuid in product:
        code = uuid.product_code
        product_name = uuid.product_name.replace(' ', '_').replace('*','_')
        barcode = Code128(code, writer=ImageWriter())
        # save the barcode to a file in the images directory
        image_dir = os.path.join(settings.BASE_DIR, 'images')
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        # change image name to product name
        barcode.save(os.path.join(image_dir, product_name), options={'background': 'white', 'foreground': 'black'})
    return JsonResponse({'success':True})


def get_product_by_uuid(request, uuid):
    if request.method == 'GET':
        product = Products.objects.get(product_code=uuid)
        data = {
            'product_name':product.product_name,
            'sales_price':product.cost,
            'product_uuid':product.product_code,
        }
        return JsonResponse(data)
    