from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User 
from django.core.validators import validate_email

class CustomUserSignupForm(UserCreationForm):

    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username'
            }
        )
    )
    email=forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Email Address'
            }
        )
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password'
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Confirm Password'
            }
        )
    )

    class Meta:
        model = User
        fields =('username','email')





def clean_confirm_password(self):
    pas=self.cleaned_data['password']
    cpas=self.cleaned_data['confirm_password']
    MIN_LENGTH=8
    if pas and cpas:
        if pas!=cpas:
            raise forms.ValidationError("password and confirm password not matched")
        else:
            if len(pas)<MIN_LENGTH:
                raise forms.ValidationError("Password should have atleast %d characters" %MIN_LENGTH)
            if pas.isdigit():
                raise forms.ValidationError("Password should not all numeric")
                




