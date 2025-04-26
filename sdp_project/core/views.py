# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from .models import Sale
from .forms  import SaleForm

# -------------- Public pages ----------------
class HomeView(TemplateView):
    template_name = 'core/home.html'

class ContactView(TemplateView):
    template_name = 'core/contact.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'

# --------- Auth pages: login/register --------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# ------ Protected pages (must be logged in) ---
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def messages(request):
    return render(request, 'core/messages.html')

# --------------- Sales CRUD -------------------
class SaleListView(LoginRequiredMixin, ListView):
    model               = Sale
    template_name       = 'core/sale_list.html'
    context_object_name = 'sales'
    paginate_by         = 10

    def get_queryset(self):
        return Sale.objects.filter(created_by=self.request.user).order_by('-date')

class SaleCreateView(LoginRequiredMixin, CreateView):
    model         = Sale
    form_class    = SaleForm
    template_name = 'core/sale_form.html'
    success_url   = reverse_lazy('sale_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class SaleUpdateView(LoginRequiredMixin, UpdateView):
    model         = Sale
    form_class    = SaleForm
    template_name = 'core/sale_form.html'
    success_url   = reverse_lazy('sale_list')