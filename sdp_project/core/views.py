from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import SaleForm ,CustomUserCreationForm, CustomAuthenticationForm
from .models import Sale
        
        
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def login(request):
    login_error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            login_error = "Invalid username or password."
    return render(request, 'core/login_and_register.html', {
        'login_error': login_error,
        'active_tab': 'login',
    })

User = get_user_model()

def register(request):
    register_error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            register_error = "Passwords do not match."
        elif User.objects.filter(username=username).exists():
            register_error = "Username already exists."
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            return redirect('login')
    return render(request, 'core/login_and_register.html', {
        'register_error': register_error,
        'active_tab': 'register',
    })

@login_required
def sale_list(request):
    sales = Sale.objects.filter(seller=request.user).order_by('-created_at')
    return render(request, 'core/browse_sale.html', { 'sales': sales })

# Create a sale
@login_required
def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.seller = request.user
            sale.save()
            return redirect('browse_sales')
    else:
        form = SaleForm()
    return render(request, 'core/create_sale.html', {'form': form})

# Edit a sale
@login_required
def sale_edit(request, pk):
    sale = get_object_or_404(Sale, pk=pk, seller=request.user)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('browse_sales')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'core/create_sale.html', {'form': form, 'sale': sale})

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')