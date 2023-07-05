from django import forms
from .models import producto_pc, producto_celulare, producto_notebook
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto_pc
        fields = '__all__'

class ProductoForm2(forms.ModelForm):
    class Meta:
        model = producto_celulare
        fields = '__all__'

class ProductoForm3(forms.ModelForm):
    class Meta:
        model = producto_notebook
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    pass
    email = forms.EmailField(label="Correo electrónico")  # Campo de correo electrónico adicional

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')