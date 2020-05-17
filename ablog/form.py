from .models import *
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'author']
        
        widgets = {
            'title' :forms.TextInput(attrs={'class': 'form-control'}),
            'body' :forms.Textarea(attrs={'class': 'form-control'}),
            'author' :forms.Select(attrs={'class': 'form-control'}),
        }

#choice = [('C','C'), ('C++','C++') ,('Java', 'Java')]
choice_list = Category.objects.all().values_list('name','name') 
choice_item = []

for item in choice_list:
    choice_item.append(item)   
class AddForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body','category', 'author']
        
        widgets = {
            'title' :forms.TextInput(attrs={'class': 'form-control'}),
            'body' :forms.Textarea(attrs={'class': 'form-control'}),
            'category' :forms.Select( choices=choice_item, attrs={'class': 'form-control'}),
            'author' :forms.Select(attrs={'class': 'form-control'}),
        }
        