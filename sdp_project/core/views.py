from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .forms import SaleForm ,CustomUserCreationForm, CustomAuthenticationForm
from .models import Sale
        
        
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def login(request):
    login_form = CustomAuthenticationForm(request, data=request.POST or None)
    login_error = None

    if request.method == 'POST':
        if login_form.is_valid():
            print("Form is vaid")
            user = login_form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
        else:
            login_error = "Invalid login credentials."
            print(login_error)
            print(login_form.errors.as_json())
    return render(request, 'core/login_and_register.html', {
        'form': login_form,
        'register_form': CustomUserCreationForm(),
        'login_error': login_error,
        'active_tab': 'login',
    })
    
    
def register(request):
    register_form = CustomUserCreationForm(request.POST or None)
    register_error = None

    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
        else:
            register_error = "Registration failed. Please check the form."

    return render(request, 'core/login_and_register.html', {
        'form': CustomAuthenticationForm(),
        'register_form': register_form,
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