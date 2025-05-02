from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home, contact, about, dashboard, login, register,
    sale_list, sale_create, sale_edit, logout
)

urlpatterns = [
    # Public pages
    path('',                        home,                            name='home'),
    path('dashboard/',              dashboard,                       name='dashboard'),
    path('about/',                  about,                           name='about'),
    path('contact/',                contact,                         name='contact'),

    # Authentication
    path('login/',                  login,              name='login'),
    path('logout/',                 logout,             name='logout'),
    path('register/',               register,              name='register'),

    # Sales (function-based)
    path('sales/',                  sale_list,                       name='browse_sales'),
    path('sales/create/',           sale_create,                     name='create_sale'),
    path('sales/<int:pk>/edit/',    sale_edit,                       name='edit_sale'),
]
