from re import A
from django.forms import ImageField, ModelForm, TextInput, ModelChoiceField, Form
from django import forms
from .models import Category, Products


class MyChoiceField(forms.ChoiceField):
    widget = forms.Select(attrs={"required": False})


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["category_name", "category_image"]
        widgets = {
            "category_name": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Catergory Name"}
            ),
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
    class MyForm(forms.ModelForm):
        unit_id = MyChoiceField(
            choices=Products.unit_name,
            widget=forms.Select(
                attrs={
                    "class": "form-control",
                    
                }
            ),
        )

    class Meta:
        model = Products
        fields = [
            "product_code",
            "product_name",
            "category_id",
            "quantity_in_stock",
            "unit_price",
            "cost",
            "reorder_level",
            "unit_id",
            "brand",
            "export_csv",
        ]

        widgets = {
            "product_code": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Code",
                    "data-errors": "Please Enter Code.",
                    "required": "required",
                }
            ),
            "product_name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Name",
                    "data-errors": "Please Enter Name.",
                    "required": "required",
                }
            ),
            "unit_in_stock": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Unit in Stock",
                }
            ),
            "unit_price": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Unit Price",
                }
            ),
            "cost": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Cost",
                }
            ),
            "reorder_level": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Reorder Level",
                }
            ),
            "brand": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Brand",
                }
            ),
         
            # "category_id":ModelChoiceField(queryset=Category.objects.all(), to_field_name="type")
        }


class FileUploadForm(Form):
    file = forms.FileField()
