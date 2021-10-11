from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic



def home(request):
    return render(request, 'webapp/index.html')


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['email']
            message = form.cleaned_data['message']
            from_email = 'contact@elysiancoder.com'
            to_email = ['aikurashina@elysiancoder.com']
            try:
                send_mail(subject, message, from_email, to_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success/')
    return render(request, "contactpage/contact.html", {'form': form})

def successView(request):
    #return HttpResponse('Success! Thank you for your message.')
    return render(request, "contactpage/success.html")
