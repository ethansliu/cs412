from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User

# Create your models here.
class Closet(models.Model):
    firstName = models.TextField(blank=False)
    lastName = models.TextField(blank=False)
    favoriteStyle = models.TextField(blank=False)
    favoriteBrand = models.TextField(blank=False)
    userWeight = models.TextField(blank=False)
    userHeight = models.TextField(blank=False)
    shirtSize = models.TextField(blank=False)
    pantSize = models.TextField(blank=False)
    outerwearSize = models.TextField(blank=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        '''Return a string representation of this Article.'''
        return f"{self.firstName} {self.lastName}'s Closet"
    
    def get_categories(self):
        '''Retrieve all comments for this Article.'''

        # use the ORM to filter Comments where this 
        # instance of Article is the FK
        category = Category.objects.filter(closet=self)
        return category
    
    def get_absolute_url(self) -> str:
        '''return the URL to redirect to after sucessful create'''
 
        return reverse('show_closet', kwargs={'pk': self.pk})

class Category(models.Model):
    closet = models.ForeignKey("Closet", on_delete=models.CASCADE)
    categoryName = models.TextField(blank=False)

    def __str__(self):
        '''Return a string representation of this Article.'''
        return f"{self.closet.firstName}'s {self.categoryName}"
    
    def get_clothes(self):
        '''Retrieve all comments for this Article.'''

        # use the ORM to filter Comments where this 
        # instance of Article is the FK
        clothe = Clothes.objects.filter(category=self)
        return clothe

class Clothes(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    brand = models.TextField(blank=False)
    color = models.TextField(blank=False)
    image = models.ImageField(blank=True)
    price = models.IntegerField(blank=False)
    size = models.TextField(blank=False)

    def __str__(self):
        '''Return a string representation of this Article.'''
        return f"{self.category.closet.firstName}'s {self.color} {self.brand} {self.category.categoryName}"
    


class Outfit(models.Model):
    outfitCreated = models.DateTimeField(auto_now=True)
    outfitName = models.TextField(blank=False)
    top = models.ForeignKey("Clothes", on_delete=models.CASCADE, related_name="top", null=True, blank=True)
    bottom = models.ForeignKey("Clothes", on_delete=models.CASCADE, related_name="bottom", null=True, blank=True)
    outerwear = models.ForeignKey("Clothes", on_delete=models.CASCADE, related_name="outerwear", null=True, blank=True)
    shoes = models.ForeignKey("Clothes", on_delete=models.CASCADE, related_name="shoes", null=True, blank=True)
    def __str__(self):
        '''Return a string representation of this Article.'''
        return f"{self.outfitName}"

class Sell(models.Model):
    item = models.ForeignKey("Clothes", on_delete=models.CASCADE)
    platform = models.TextField(blank=True)
    sellPrice = models.IntegerField(blank=False)

    def __str__(self):
        '''Return a string representation of this Article.'''
        return f"{self.item} for sale"
    
    def get_clothes(self):
        '''Retrieve all comments for this Article.'''

        # use the ORM to filter Comments where this 
        # instance of Article is the FK
        return Clothes.objects.filter(id=self.item.id)
