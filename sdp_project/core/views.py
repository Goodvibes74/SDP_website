from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import Sale
from django.db.models.functions import TruncMonth
from django.db.models import Sum

        
        
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
            return redirect('home')
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
    print(sales)
    return render(request, 'core/browse_sale.html', { 'sales': sales})

# Create a sale
@login_required
def sale_create(request):
    error = None
    if request.method == 'POST':
        print("Entered post")
        customer = request.POST.get('customer')  # FIXED: was 'title', should be 'customer'
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        status = request.POST.get('status', 'pending')
        if not customer or not description or not amount or not status:
            error = "All fields are required."
            print("Fied missing")
        else:
            try:
                amount = float(amount)
                sale = Sale.objects.create(
                    customer=customer,
                    description=description,
                    amount=amount,
                    seller=request.user,
                    status=status
                )
                print(sale)
                print("Success")
                return redirect('browse_sales')
            except ValueError:
                error = "Amount must be a number."
                
    print("We have errors")   
    return render(request, 'core/create_sale.html', {'error': error, 'sale': None, 'status_choices': Sale.STATUS_CHOICES})

# Edit a sale
@login_required
def sale_edit(request, pk):
    sale = get_object_or_404(Sale, pk=pk, seller=request.user)
    error = None
    success = None

    if request.method == 'POST':
        # Only update fields that are present in the POST data
        updated = False
        customer = request.POST.get('customer')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        status = request.POST.get('status')

        if customer is not None and customer != sale.customer:
            sale.customer = customer
            updated = True
        if description is not None and description != sale.description:
            sale.description = description
            updated = True
        if amount is not None:
            try:
                amount_val = float(amount)
                if amount_val != float(sale.amount):
                    sale.amount = amount_val
                    updated = True
            except ValueError:
                error = "Amount must be a number."
        if status is not None and status != sale.status:
            sale.status = status
            updated = True
        if not error and updated:
            sale.save()
            success = "Sale updated successfully!"
        elif not error and not updated:
            success = "No changes detected."
        elif error:
            pass
    return render(request, 'core/create_sale.html', {
        'sale': sale,
        'error': error,
        'success': success,
        'status_choices': Sale.STATUS_CHOICES
    })

def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk, seller=request.user)
    if request.method == 'POST':
        sale.delete()
        return redirect('browse_sales')
    return render(request, 'core/sale_delete.html', {'sale': sale})

@login_required
def dashboard(request):
    user = request.user
    sales = Sale.objects.filter(seller=user)

    # Totals
    total_sales      = sales.count()
    active_sales     = sales.filter(status='active').count()
    pending_sales    = sales.filter(status='pending').count()
    completed_sales  = sales.filter(status='completed').count()
    
    recent_sales = sales.order_by('-created_at')[:5]

    cards = [
        { 'icon': 'bi-bar-chart-fill',    'color': 'text-primary', 'title': 'Total Sales',     'value': total_sales     },
        { 'icon': 'bi-bag-check-fill',     'color': 'text-success', 'title': 'Active Sales',    'value': active_sales    },
        { 'icon': 'bi-clock-history',      'color': 'text-warning', 'title': 'Pending Sales',   'value': pending_sales   },
        { 'icon': 'bi-check-circle-fill',  'color': 'text-success', 'title': 'Completed Sales', 'value': completed_sales },
    ]

    return render(request, 'core/dashboard.html', {
        'user':           user,
        'cards':          cards,
        'recent_sales':   recent_sales,
    })
    
@login_required
def update(request, sale_id):
    error = None
    sale = get_object_or_404(Sale, id=sale_id, seller=request.user)
    if request.method == 'POST':
        print("Entered post")
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        status = request.POST.get('status', 'pending')
        if not description or not amount or not status:
            error = "All fields are required."
            print("Field missing")
        else:
            try:
                amount = float(amount)
                sale.description = description
                sale.amount = amount
                sale.status = status
                sale.save()
                print("Success")
                return redirect('browse_sales')
            except ValueError:
                error = "Amount must be a number."
                
    print("We have errors")   
    return render(request, 'core/create_sale.html', {'error': error, 'sale': sale, 'status_choices': Sale.STATUS_CHOICES})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')