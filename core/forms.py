import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.validators import MinLengthValidator

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(
        required=True,
        validators=[MinLengthValidator(3)],
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        help_text="Required. Minimum 3 characters. Letters, digits and @/./+/-/_ only.",
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
