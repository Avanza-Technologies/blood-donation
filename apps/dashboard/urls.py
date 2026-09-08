from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('donor/', views.donor_dashboard, name='donor_dashboard'),
    path('customer/', views.customer_dashboard, name='customer_dashboard'),
]
