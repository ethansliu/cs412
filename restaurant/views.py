from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpRequest, HttpResponse
import time
import random
import datetime


# Create your views here.
def main(request):
    '''
    A function to respond to the /hw URL.
    This function will delegate work to an HTML template.
    '''
    # this template will present the response
    template_name = "restaurant/main.html"

    # create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
        'letter1' : chr(random.randint(65,90)), # a letter in the range A ... Z
        'letter2' : chr(random.randint(65,90)), # a letter in the range A ... Z
        'number' : random.randint(1,10), # a number in the range 1...10
    }

    # delegate response to the template:
    return render(request, template_name, context)

def order(request):
    '''Show the HTML form to the client.'''
    daily_special = random.choice(["Pizza Lobster", "Zucchini Fritti", "Pizza Shrimp Scampi", "Pizza Clam", "Apple Cider Tiramisu", "Limoncello Cranberry Cake"])
    # use this template to produce the response
    context = {
        'daily_special': daily_special,
        'menu_items': [
            {'name': 'Pizza Margherita', 'price': 16},
            {'name': 'Pizza Spicy Soppressata', 'price': 19},
            {'name': 'Pizza Porcini and Chantrelle', 'price': 19},
            {'name': 'Raddichio Salad', 'price': 9},
            {'name': 'Homemade Limonata', 'price': 4},
            {'name': daily_special, 'price': 20},  # Daily special included in the menu
        ]
    }
    template_name = 'restaurant/order.html'
    return render(request, template_name, context)

def confirmation(request):
    '''
    Handle the form submission. 
    Read out the form data. 
    Generate a response.
    '''
    template_name = 'restaurant/confirmation.html'
    # print(request)
    
    # check if the request is a POST (vs GET)
    if request.POST:
        selected_items = request.POST.getlist('items') 
        salad_addons = request.POST.getlist('salad_addons')
        customer_name = request.POST.get('name')
        customer_phone = request.POST.get('phone')
        customer_email = request.POST.get('email')
        special_instructions = request.POST.get('instructions')

        menu_items = {
            "Pizza Lobster": 20,
            "Zucchini Fritti": 20,
            "Pizza Shrimp Scampi": 20,
            "Pizza Clam": 20,
            "Apple Cider Tiramisu": 20,
            "Limoncello Cranberry Cake": 20,
            "Pizza Margherita": 16,
            "Pizza Spicy Soppressata": 19,
            "Pizza Porcini and Chantrelle": 19,
            "Raddichio Salad": 9,
            "Homemade Limonata": 4,
        }

        salad_addons = {
            "Chicken Breast" : 6,
            "Steak" : 8,
            "Mushrooms" : 4,
        }

        ordered_items = [(item, menu_items[item]) for item in selected_items if item in menu_items]

        if 'Raddichio Salad' in selected_items and salad_addons:
            for addon in salad_addons:
                ordered_items.append((addon, salad_addons[addon]))

        total_price = sum(price for item, price in ordered_items)

        current_time = time.time()  # Current time in seconds since epoch
        minutes_to_add = random.randint(30, 60)  # Random number between 30 and 60 minutes
        ready_time_in_seconds = current_time + minutes_to_add * 60  # Convert minutes to seconds

        # Convert back to a human-readable time
        ready_time_struct = time.localtime(ready_time_in_seconds)
        ready_time = time.strftime("%I:%M %p", ready_time_struct)



        # package the data up to be used in response
        context = {
            'customer_name': customer_name,
            'customer_phone': customer_phone,
            'customer_email': customer_email,
            'special_instructions': special_instructions,
            'selected_items': selected_items,
            'ordered_items': ordered_items,
            'total_price': total_price,
            'ready_time': ready_time,  # Format the time nicely
        }

        # generate a response
        return render(request, template_name, context)

    ## GET lands down here: no return statements!

    # this is an OK solution: a graceful failure
    # return HttpResponse("Nope.")

    # if the client got here by making a GET on this URL, send back the form
    # use this template to produce the response

    # this is a "better solution", but shows the wrong URL
    # template_name = 'formdata/form.html'
    # return render(request, template_name)

    # this is the "best" solution: redirect to the correct URL
    return redirect("confirmation")