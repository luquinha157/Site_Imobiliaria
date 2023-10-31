from django.shortcuts import render
from django import forms


class LoginForms(forms.Form):
    email=forms.EmailField(
        label='Email', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: jose@django.com',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

class RegisterForms(forms.Form):
    name=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )
    password=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )
    password_confirm=forms.CharField(
        label='Confirme a sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        ),
    )

    def clean_name_register(self):
        name = self.cleaned_data.get('name')

        if name:
            name = name.strip()
            if ' ' in name:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return name

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return password_confirm

class MessageSend(forms.Form):
    nome_form = forms.CharField(
        label='Nome',
        required= True,
        max_length= 45,
        widget= forms.TextInput(
            attrs = {
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'form3Example1c'
            }
        )
    )
    email_form = forms.EmailField(
        label = 'Email',
        required = True,
        max_length = 60,
        widget = forms.EmailInput(
            attrs = {
                'type' : 'email',
                'class' : 'form-control',
                'id' : 'form3Example3c',
                'placeholder' : 'email@email.com',
            }
        )
    )
    subject_form = forms.CharField(
        label='Endereço',
        required= True,
        max_length= 14,
        widget= forms.TextInput(
            attrs = {
                'type' : 'text',
                'class' : 'form-control',
            }
        )
    )
    message_form = forms.CharField(
        label='Telefone',
        required= True,
        max_length= 255,
        widget= forms.TextInput(
            attrs = {
                'type' : 'text',
                'class' : 'form-control',
            }
        )
    )


