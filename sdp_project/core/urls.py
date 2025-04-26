from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView, ContactView, AboutView,
    dashboard, messages, register,
    SaleListView, SaleCreateView, SaleUpdateView
)

urlpatterns = [
    path('',               HomeView.as_view(),      name='home'),
    path('contact/',       ContactView.as_view(),   name='contact'),
    path('about/',         AboutView.as_view(),     name='about'),

    path('login/',         auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',        auth_views.LogoutView.as_view(), name='logout'),
    path('register/',      register,                name='register'),

    path('dashboard/',     dashboard,               name='dashboard'),
    path('messages/',      messages,                name='messages'),

    path('sales/',         SaleListView.as_view(),   name='sale_list'),
    path('sales/add/',     SaleCreateView.as_view(), name='sale_add'),
    path('sales/<int:pk>/edit/', SaleUpdateView.as_view(), name='sale_edit'),
]
