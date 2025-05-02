from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home, contact, about, dashboard, login, register,
    sale_list, sale_create, sale_edit, sale_delete, logout,
)

urlpatterns = [
    # Public pages accessible to all users
    path('',                        home,                            name='home'),
    path('dashboard/',              dashboard,                       name='dashboard'),
    path('about/',                  about,                           name='about'),
    path('contact/',                contact,                         name='contact'),

    # Authentication views 
    path('login/',                  login,                           name='login'),
    path('logout/',                 logout,                          name='logout'),
    path('register/',               register,                        name='register'),

    # Sales (function-based-views were used here for simplicity)
    # These views are protected by the login_required decorator and are only accessible to logged-in users
    path('sales/',                  sale_list,                       name='browse_sales'),
    path('sales/create/',           sale_create,                     name='create_sale'),
    path('sales/<int:pk>/edit/',    sale_edit,                       name='edit_sale'),
    path('sales/<int:pk>/delete/',  sale_delete,                     name='delete_sale'),
]
