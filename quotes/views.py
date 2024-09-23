from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random


quotes = ["Be a yardstick of quality. Some people aren't used to an environment where excellence is expected.",
          "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma - which is living with the results of other people's thinking. Don't let the noise of others' opinions drown out your own inner voice. And most important, have the courage to follow your heart and intuition.",
          "Stay hungry, stay foolish.",
          "When you're a carpenter making a beautiful chest of drawers, you're not going to use a piece of plywood on the back, even though it faces the wall and nobody will ever see it. You'll know it's there, so you're going to use a beautiful piece of wood on the back."
          ]

images = [
          "steve-jobs-photos-by-norman-seeff-1.png",
          "10productsth.png",
          "profoto-albert-watson-steve-jobs-pinned-image-original.png",
          "Steve_Jobs_Headshot_2010-CROP_(cropped_2).png",
          "104534890-steve-jobs-1.png"
          ]


# Create your views here.
def home(request):
    '''
    A function to respond to the /hw URL.
    This function will delegate work to an HTML template.
    '''
    # this template will present the response
    template_name = "quotes/home.html"

    # create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
        'letter1' : chr(random.randint(65,90)), # a letter in the range A ... Z
        'letter2' : chr(random.randint(65,90)), # a letter in the range A ... Z
        'number' : random.randint(1,10), # a number in the range 1...10
    }

    # delegate response to the template:
    return render(request, template_name, context)

def about(request):
    '''
    A function to respond to the /hw/about URL.
    This function will delegate work to an HTML template.
    '''
    # this template will present the response
    template_name = "quotes/about.html"

    # create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
    }

    # delegate response to the template:
    return render(request, template_name, context)

def quote(request):
    selectedQuote = random.choice(quotes)
    selectedImage = random.choice(images)
    quoteAndImg = {
        'quote': selectedQuote,
        'image': selectedImage
    }
    return render(request, 'quotes/quote.html', quoteAndImg)

def show_all(request):
    quoteAndImg = {
        'quotes': quotes,
        'images': images
    }
    return render(request, 'quotes/show_all.html', quoteAndImg)