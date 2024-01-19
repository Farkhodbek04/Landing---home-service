from django.shortcuts import render
from main import models
from .models  import Services, Clients, Contacts

def index(request):
    services = models.Services.objects.all()
    clients = models.Clients.objects.all()
    contacts = models.Contacts.objects.all()

    context = {
        'services':services,
        'clients':clients,
        'contacts':contacts
    }
    return render(request, 'front/index.html', context)

def about(request):

    return render(request, 'front/contact.html')

def contact(request):
    return render(request, 'front/index.html')

def service(request):
    return render(request, 'front/service.html')


