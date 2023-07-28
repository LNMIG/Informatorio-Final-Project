from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = models.Articulo
        fields = ['titulo', 'bajada', 'contenido',
                  'imagen', 'categoria', 'etiquetas']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'bajada': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'etiquetas': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = models.Comentario
        fields = ['contenido']

        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'id':'textAreaExample', 'style':"background: #fff;"}),
        }

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Usuario',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repetir Contraseña',
    }))

    def clean_email(self):
        email_recibido = self.cleaned_data.get("email")
        correo_ya_registrado = User.objects.filter(email = email_recibido).exists()
        user_es_activo = User.objects.filter(email = email_recibido, is_active = 1)
        if correo_ya_registrado and user_es_activo:
            raise forms.ValidationError("Correo electrónico ya registrado.")
        elif correo_ya_registrado:
            User.objects.filter(email = email_recibido).delete()

        return email_recibido