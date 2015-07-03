from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
from contact.forms import ContactForm
from contact.models import Contact

def contact(request):
    form = ContactForm(request.GET or None)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = form.data.get('name')
        email = form.data.get('email')
        subject = form.data.get('subject')
        message = form.data.get('message')

        try:
            contact = Contact(name=name, email=email, suject=subject, message=message)
            #saving in DB
            contact.save()
        except Exception as e:
            msg_error = e

    return render_to_response('contact.html', locals(), context_instance=RequestContext(request))