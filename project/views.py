from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from typing import Any

# Create your views here.

from . models import * 
from . forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


class ShowHomeView(TemplateView):
    template_name = "project/home_page.html"

class ShowClosetView(LoginRequiredMixin, DetailView):
    model = Closet
    template_name = "project/show_closet.html"
    context_object_name = 'closet'

class ShowCategoryView(DetailView):
    model = Category
    template_name = "project/show_category.html"
    context_object_name = 'category'

class CreateCategoryView(CreateView):
    form_class = CreateCategoryForm
    template_name = "project/create_category_form.html"

    def form_valid(self, form):
        # Get the closet ID from the URL
        closet_id = self.kwargs['pk']
        closet = get_object_or_404(Closet, pk=closet_id)
        # Assign the closet to the category
        form.instance.closet = closet
        # Save the form
        self.object = form.save()
        # Redirect to the show_closet page after successful creation
        return redirect(reverse('show_closet', kwargs={'pk': closet.pk}))

    def get_context_data(self, **kwargs):
        # Add closet context for use in the template
        context = super().get_context_data(**kwargs)
        closet_id = self.kwargs['pk']
        context['closet'] = get_object_or_404(Closet, pk=closet_id)
        return context

class UpdateCategoryView(UpdateView):
    model = Category
    template_name = "project/update_category_form.html"
    fields = ['categoryName',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the category object to the template
        context['category'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the closet page after successful update
        return reverse('show_closet', kwargs={'pk': self.object.closet.pk})


class DeleteCategoryView(DeleteView):
    model = Category 
    template_name = "project/delete_category_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the category object to the template
        context['category'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the closet page after successful deletion
        return reverse('show_closet', kwargs={'pk': self.object.closet.pk})


class ShowClothesView(DetailView):
    model = Clothes
    template_name = "project/show_clothes.html"
    context_object_name = 'clothes'

    
class CreateClothesView(CreateView):
    form_class = CreateClothesForm
    template_name = "project/create_clothes_form.html"

    def form_valid(self, form):
        # Get the category ID from the URL
        category_id = self.kwargs['pk']
        category = get_object_or_404(Category, pk=category_id)
        # Assign the category to the clothing item
        form.instance.category = category
        # Save the form
        self.object = form.save()
        # Redirect to the show_category page after successful creation
        return redirect(reverse('show_category', kwargs={'pk': category.pk}))

    def get_context_data(self, **kwargs):
        # Add category context for use in the template
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['pk']
        context['category'] = get_object_or_404(Category, pk=category_id)
        return context

class UpdateClothesView(UpdateView):
    model = Clothes
    template_name = "project/update_clothes_form.html"
    fields = ['brand', 'color', 'image', 'price', 'size']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the clothes object to the template
        context['clothes'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the category page after successful update
        return reverse('show_category', kwargs={'pk': self.object.category.pk})

class DeleteClothesView(DeleteView):
    model = Clothes
    template_name = "project/delete_clothes_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the clothes object to the template
        context['clothes'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the category page after successful deletion
        return reverse('show_category', kwargs={'pk': self.object.category.pk})


class ShowSellClothesView(ListView):
    model = Sell
    template_name = "project/show_sell_clothes.html"
    context_object_name = 'sell'


class CreateSellClothesView(CreateView):
    form_class = CreateSellClothesForm
    template_name = "project/create_sell_form.html"

    def form_valid(self, form):
        # Save the form
        self.object = form.save()
        # Redirect to the sell page after successful creation
        return redirect(reverse('sell_clothes'))

    def get_context_data(self, **kwargs):
        # Add context for use in the template
        context = super().get_context_data(**kwargs)
        return context


class UpdateSellClothesView(UpdateView):
    model = Sell
    template_name = "project/update_sell_clothes_form.html"
    fields = ['platform', 'sellPrice']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the sell object to the template
        context['sell'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the sell page after successful update
        return reverse('sell_clothes')

class DeleteSellClothesView(DeleteView):
    model = Sell
    template_name = "project/delete_sell_clothes_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the sell object to the template
        context['sell'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the sell page after successful deletion
        return reverse('sell_clothes')

class ShowOutfitView(ListView):
    model = Outfit
    template_name = "project/show_outfit.html"
    context_object_name = 'outfits'

class ShowOutfitDetailView(DetailView):
    model = Outfit
    template_name = "project/show_outfit_detail.html"
    context_object_name = 'outfit_detail'

class CreateOutfitView(CreateView):
    form_class = CreateOutfitForm
    template_name = "project/create_outfit_form.html"

    def form_valid(self, form):
        # Save the form
        self.object = form.save()
        # Redirect to the outfit list page after successful creation
        return redirect(reverse('show_outfits'))

    def get_context_data(self, **kwargs):
        # Add context for use in the template
        context = super().get_context_data(**kwargs)
        return context
    
class UpdateOutfitView(UpdateView):
    model = Outfit
    template_name = "project/update_outfit_form.html"
    fields = ['outfitName', 'top', 'bottom', 'outerwear', 'shoes']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the outfit object to the template
        context['outfit'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the outfit list page after successful update
        return reverse('show_outfits')

class DeleteOutfitView(DeleteView):
    model = Outfit
    template_name = "project/delete_outfit_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the outfit object to the template
        context['outfit'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the outfit list page after successful deletion
        return reverse('show_outfits')
