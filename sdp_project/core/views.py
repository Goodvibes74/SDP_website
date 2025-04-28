from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SaleForm
from .models import Sale
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
        
        
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def login_and_register(request):
    # Initialize the login and registration forms
    login_form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == 'POST':
        # Handle login form submission
        if 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                # Authenticate and log in the user
                user = login_form.get_user()
                login(request, user)
                return redirect('dashboard')
        # Handle registration form submission
        elif 'register' in request.POST:
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                # Save the new user and redirect to login
                register_form.save()
                return redirect('login')

    # Render the login and registration page with the forms
    return render(request, 'core/login_and_register.html', {
        'form': login_form,
        'register_form': register_form,
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
