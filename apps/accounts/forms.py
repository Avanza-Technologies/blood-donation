from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class DonorRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.DONOR
        user.is_active = False # Pending admin approval
        if commit:
            user.save()
            # We will create the DonorProfile in the future phase
        return user

class CustomerRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.CUSTOMER
        if commit:
            user.save()
            # We will create the CustomerProfile in the future phase
        return user
