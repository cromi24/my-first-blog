from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            ]

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class SignUpForm(UserCreationForm):
   def clean(self):
       username = self.cleaned_data.get('username')
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
           raise ValidationError("Такой Email уже используется другим пользователем!")
       if User.objects.filter(username=username).exists():
           raise ValidationError("Это имя уже занято!")
       return self.cleaned_data

   class Meta:
       model = User
       fields = [
           'username',
           'email',
           'password1',
           'password2',
            ]