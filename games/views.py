from django.shortcuts import render
from .models import Game
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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

def login_page(request):  # username, password
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        print(user)
        
        if user is not None:
            login(request, user)
            print('User logged in')
            return render(request, 'index.html')
        else:
            print('User not found')
            return render(request, 'login.html')
    return render(request, 'login.html')



def register_page(request):  # full_name, username, email, telefon, password, confirm_password
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        telefon = request.POST.get('telefon')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = full_name
            user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'register.html')
    return render(request, 'register.html')

