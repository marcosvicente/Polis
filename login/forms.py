#_*_ coding: utf-8 _*_
from django import forms 
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserForms(forms.ModelForm): 
    User._meta.get_field('username').blank = False
    User._meta.get_field('first_name').blank = False
    User._meta.get_field('email').blank = False
    User._meta.get_field('password').blank = False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets ={
                'username' : forms.TextInput(attrs ={'placeholder':'Digite seu username:'}),
                'first_name':forms.TextInput(attrs={'placeholder':'Digite seu primeiro nome:'}),
                'last_name':forms.TextInput(attrs={'placeholder':'Digite seu segundo nome'}),
                'email':forms.TextInput(attrs={'placeholder': 'Digite seu email'}),
                'password': forms.TextInput(attrs={'type':'password',
                    'placeholder': 'Digite sua senha'}
                    ),
                } 
        error_messages ={
                'username':{
                    'required':'Este campo é obrigatório'
                    },
                'first_name':{
                    'required':'Este campo é obrigatório'
                    },
                'last_name':{
                    'required':'Este campo é obrigatório'
                    },
                'email':{
                        'required':'Este campo é obrigatório'
                    },
                'password':{
                    'required':'Este campo é obrigatório'
                    }
            }
        def save(self, commit):
            user = super(UserForms, self).save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
