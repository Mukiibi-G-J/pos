
from re import A
from django.forms import ImageField, ModelForm, TextInput,ModelChoiceField, Form
from django import forms
from .models import Category, Products

 

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields=['category_name', 'category_image']
        widgets={
            'category_name':TextInput(attrs={
                'class':"form-control",
                'placeholder':'Enter Catergory Name'
                
            }),
            # 'category_id':TextInput(attrs={
            #     C
            #     'placeholder':'Enter Code'
            # }),
             # 'category_image':TextInput(attrs={
             #     "type":"file",
             #    'class':"form-control image-file",
             #    'placeholder':'Enter Code'
            # }
            # )           
        }
        
        
class AddProductForm(ModelForm):
    class Meta:
        model = Products
        fields =['product_code','product_name',
        'unit_id','category_id','unit_in_stock',
        'unit_price','cost','reorder_level',
        'brand','export_csv']
        widgets={
        'product_code':TextInput(attrs={
            'class':"form-control",
              "placeholder":"Enter Code",
              "data-errors":"Please Enter Code.",
              "required":"required",
    

            }),
        'product_name':TextInput(attrs={
            'class':"form-control",
            "placeholder":"Enter Name",
            "data-errors":"Please Enter Name.",
            "required":"required",

            }),
        "unit_in_stock":TextInput(attrs={
              'class':"form-control",

            }),

        "unit_price":TextInput(attrs={}),
      
        "cost":TextInput(attrs={
               'class':"form-control",

            }),
        "reorder_level":TextInput(attrs={
             'class':"form-control",

            }),
        'brand':TextInput(attrs={
            'class':"form-control",

            }),
        # "category_id":ModelChoiceField(queryset=Category.objects.all(), to_field_name="type")

        }




class FileUploadForm(Form):
    file = forms.FileField()