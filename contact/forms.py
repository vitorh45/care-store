# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome',max_length=100,
                           widget= forms.TextInput(attrs={'placeholder':'Nome'})
                           )
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
    subject = forms.CharField(label='Assunto', max_length=100,
                              widget=forms.TextInput(attrs={'placeholder':'Assunto'})
                              )
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'placeholder':'Mensagem'}))