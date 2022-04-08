
from re import A
from django.forms import ImageField, ModelForm, TextInput
from . models import Category

 

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields=['category_id', 'category_name', 'category_image']
        widgets={
            'category_name':TextInput(attrs={
                'class':"form-control",
                'placeholder':'Enter Catergory Name'
                
            }),
            'category_id':TextInput(attrs={
                'class':"form-control",
                'placeholder':'Enter Code'
            }),
             'category_image':TextInput(attrs={
                 "type":"file",
                'class':"form-control image-file",
                'placeholder':'Enter Code'
            })
           

            
                
           
        }
        
        
        # attrs={
        #                 "type":"file",
        #                 'class':"form-control image-file",
        #                 "name":"pic",
                        
        #     }
        
        




