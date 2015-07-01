from django.shortcuts import render

# Create your views here.
from contact.forms import ContactForm


def contatc(request):
    form = ContactForm(request.GET or None)
    return render(request, 'contatc.html', locals())