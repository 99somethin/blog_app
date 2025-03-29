from django.forms import ModelForm
from apps.categories.models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']