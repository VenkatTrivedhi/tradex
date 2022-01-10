import datetime
import time

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import User,Post
from django import forms
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):
    username = forms.CharField(label="username",
                 widget=forms.TextInput(attrs={"class": "form-input","placeholder":"username"}))
    first_name = forms.CharField(label="first name",
                 widget=forms.TextInput(attrs={"class": "form-input","placeholder":"first name"}))
    last_name = forms.CharField(label="last name",
                 widget=forms.TextInput(attrs={"class": "form-input","placeholder":"last name"}))
    email = forms.EmailField(label="email",
                widget=forms.EmailInput(attrs={"class": "form-input","placeholder":"email@mail.com"}))
    password1 = forms.CharField(label="password",
                widget=forms.PasswordInput(attrs={"class": "form-input","placeholder":"password"}))
    password2 = forms.CharField(label="confirm password",
                widget=forms.PasswordInput(attrs={"class": "form-input","placeholder":"confirm password"}))

    class Meta: 
        model= User
        fields = ('first_name','last_name','username','email','password1','password2')

    def username_clean(self):
        if self.is_valid():  
            username = self.cleaned_data['username'].lower()  
            new = User.objects.filter(username = username)  
            if new.count():  
                return "Username not avilable"  
            return username 
        return "form is not valid" 
  
    def email_clean(self):
        if self.is_valid(): 
            email = self.cleaned_data['email'].lower()  
            new = User.objects.filter(email=email)  
            if new.count():  
                return " Email Already Exist"  
            return email  
        return "form is not valid"
  
    def clean_password2(self):
        if self.is_valid():  
            password1 = self.cleaned_data['password1']  
            password2 = self.cleaned_data['password2']  
    
            if password1 and password2 and password1 != password2:  
                return "Password don't match"  
            return password2 
        return "form is not valid"



class LoginForm(forms.Form):
    username = forms.CharField(label="username", widget=forms.TextInput(attrs={"class": "form-input","placeholder":"username"}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={"class": "form-input","placeholder":"password"}))


class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-textarea","placeholder":"type here"}))

    def save(self,request):
        self.is_valid()
        text = self.cleaned_data.get('text')
        user = request.user
        created_at = datetime.datetime.now()

        post = Post(
            text=text,
            user=user,
            created_at=created_at,
        )
        post.save()

        return post


