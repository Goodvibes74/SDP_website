from django.urls import path
from .views import (
    home, contact, about, dashboard, login, register,
    sale_list, sale_create, sale_edit, sale_delete, logout,update
)

urlpatterns = [
    # Public pages accessible to all users
    path('',                                home,                            name='home'),
    path('about/',                          about,                           name='about'),
    path('contact/',                        contact,                         name='contact'),

    # Authentication views 
    path('login/',                          login,                           name='login'),
    path('logout/',                         logout,                          name='logout'),
    path('register/',                       register,                        name='register'),

    
    # Pages accessible only to authenticated users
    path('dashboard/',                      dashboard,                       name='dashboard'),
    path('sales/',                          sale_list,                       name='browse_sales'),
    path('sales/create/',                   sale_create,                     name='create_sale'),
    path('sales/update/<int:sale_id>/',     update,                          name='update_sale'),
    path('sales/<int:pk>/edit/',            sale_edit,                       name='edit_sale'),
    path('sales/<int:pk>/delete/',          sale_delete,                     name='delete_sale'),
]
