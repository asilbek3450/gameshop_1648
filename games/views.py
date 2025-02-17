from django.shortcuts import render
from .models import Game

# Create your views here.
def home_page(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    
    return render(request, 'index.html', context)

def products_page(request):
    games = Game.objects.all()
    context = {
        'abduqahhor': games
    }
    return render(request, 'product.html', context)

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

def remote_page(request):
    return render(request, 'remot.html')

def video_page(request):
    return render(request, 'video.html')
