from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .models import CustomUser
from .forms import DonorRegistrationForm, CustomerRegistrationForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if user.role == CustomUser.Role.ADMIN:
            return reverse_lazy('dashboard:admin_dashboard')
        elif user.role == CustomUser.Role.DONOR:
            return reverse_lazy('dashboard:donor_dashboard')
        elif user.role == CustomUser.Role.CUSTOMER:
            return reverse_lazy('dashboard:customer_dashboard')
        return super().get_success_url()


def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('accounts:login')


class DonorRegistrationView(CreateView):
    model = CustomUser
    form_class = DonorRegistrationForm
    template_name = 'accounts/register_donor.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Donor registration successful. Please wait for administrator approval.')
        return response


class CustomerRegistrationView(CreateView):
    model = CustomUser
    form_class = CustomerRegistrationForm
    template_name = 'accounts/register_customer.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Customer registration successful. You can now log in.')
        return response
