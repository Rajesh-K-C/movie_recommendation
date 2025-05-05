from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.validators import MinLengthValidator, RegexValidator

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

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="First Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your first name',
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-primary',
        }),
        validators=[
            RegexValidator(r'^[a-zA-Z]+$', 'Only letters are allowed.'),
            MinLengthValidator(2)
        ]
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Last Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your last name',
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-primary',
        }),
        validators=[
            RegexValidator(r'^[a-zA-Z]+$', 'Only letters are allowed.'),
            MinLengthValidator(2)
        ]
    )

    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-primary',
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
      def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-primary",
                'placeholder': field.label
            })