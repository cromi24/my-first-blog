from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Введите действующий email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            ]