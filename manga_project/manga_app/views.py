"""
Views for the Manga Creators community.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import MangaPost


def index(request):
    """
    Display the home page with the most recent manga/anime post.
    Shows a login prompt in the top-right corner.
    """
    # Get the most recent post, or None if no posts exist
    latest_post = MangaPost.objects.first()
    context = {
        'latest_post': latest_post,
    }
    return render(request, 'index.html', context)


def register(request):
    """
    Handle user registration.
    Allows new users to create an account.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Validation
        if password != password_confirm:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    """
    Handle user login.
    Allows returning users to log in.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'login.html')


def logout_view(request):
    """Handle user logout."""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')


def about(request):
    """
    Display the About page with community guidelines and expectations.
    Explains the purpose of the website.
    """
    return render(request, 'about.html')
