from django.shortcuts import render
from .models import cat
def menu(request):
    categories = cat.objects.all()  # Get all categories
    return render(request, 'menu.html', {'categories': categories})

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def order(request):
    return render(request, 'order.html')

def confirm(request):
    return render(request, 'confirm.html')
