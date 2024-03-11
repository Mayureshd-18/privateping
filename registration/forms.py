from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from chat.models import UserProfile


class SignUpForm(forms.Form):

    username = forms.CharField(min_length=5, max_length=20)
    name = forms.CharField(max_length=25, label="Name")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


