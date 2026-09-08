from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/donor/', views.DonorRegistrationView.as_view(), name='register_donor'),
    path('register/customer/', views.CustomerRegistrationView.as_view(), name='register_customer'),
]
