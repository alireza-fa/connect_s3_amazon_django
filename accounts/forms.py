from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'password'}))

    def __init__(self, request, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.request = request

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                return login(request=self.request, user=user)
            raise forms.ValidationError('username or password is wrong')


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            user = User.objects.filter(username=username)
            if user.exists():
                raise forms.ValidationError('this username already exist.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('password must be more than or equal 8 chars.')
        return password

    def save(self):
        cd = self.cleaned_data
        user = User.objects.create_user(username=cd.get('username'), password=cd.get('password'))
        return user
