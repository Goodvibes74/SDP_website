from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home, contact, about, dashboard, login_and_register,
    sale_list, sale_create, sale_edit
)

urlpatterns = [
    # Public pages
    path('',                        home,                            name='home'),
    path('dashboard/',              dashboard,                       name='dashboard'),
    path('about/',                  about,                           name='about'),
    path('contact/',                contact,                         name='contact'),

    # Authentication
    path('login/',                  login_and_register,              name='login'),
    path('logout/',                 auth_views.LogoutView.as_view(), name='logout'),
    path('register/',               login_and_register,              name='register'),

    # Sales (function-based)
    path('sales/',                  sale_list,                       name='browse_sales'),
    path('sales/create/',           sale_create,                     name='create_sale'),
    path('sales/<int:pk>/edit/',    sale_edit,                       name='edit_sale'),
]
