from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from profile.models import Profile


class SignUpForm(UserCreationForm):
    fio = forms.CharField(max_length=150)
    phone = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('fio', 'phone', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        print(User.objects.filter(email=email))
        if User.objects.filter(email=email):
            raise ValidationError('User with the same email already exist')
        return email


class ProfileEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ('fio', 'phone', 'email', 'city', 'birthday',
                  'about_yourself', 'status', 'avatar')
