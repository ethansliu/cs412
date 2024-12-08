from django import forms
from .models import Clothes, Category, Sell, Outfit

class CreateClothesForm(forms.ModelForm):

    brand = forms.CharField(label="Brand", required=True)
    color = forms.CharField(label="Color", required=True)
    image = forms.ImageField(label="Image", required=False)
    price = forms.DecimalField(label="Price", required=True, max_digits=10, decimal_places=2)
    size = forms.CharField(label="Size", required=True)

    class Meta:
        model = Clothes
        fields = ['brand', 'color', 'size', 'price', 'image', ]


class CreateSellClothesForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=Clothes.objects.all(), label="Clothing Item", required=True)
    platform = forms.CharField(label="Platform", required=True)
    sellPrice = forms.DecimalField(label="Sell Price", required=True, max_digits=10, decimal_places=2)

    class Meta:
        model = Sell
        fields = ['item', 'platform', 'sellPrice']

class CreateCategoryForm(forms.ModelForm):
    categoryName = forms.CharField(label="Category Name", required=True)

    class Meta:
        model = Category
        fields = ['categoryName']

class CreateOutfitForm(forms.ModelForm):
    outfitName = forms.CharField(label="Outfit Name", required=True)
    top = forms.ModelChoiceField(queryset=Clothes.objects.all(), label="Top", required=False)
    bottom = forms.ModelChoiceField(queryset=Clothes.objects.all(), label="Bottom", required=False)
    outerwear = forms.ModelChoiceField(queryset=Clothes.objects.all(), label="Outerwear", required=False)
    shoes = forms.ModelChoiceField(queryset=Clothes.objects.all(), label="Shoes", required=False)

    class Meta:
        model = Outfit
        fields = ['outfitName', 'top', 'bottom', 'outerwear', 'shoes']
