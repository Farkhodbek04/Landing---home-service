from django.shortcuts import render, redirect
from main import models
from .models  import Services, Clients, Contacts
from django.contrib.auth.models import User

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

# Dashboard
def dashboard(request):
    return render(request, 'dashboard/index.html')

# Services

def services(request):
    services = models.Services.objects.all()
    return render(request, 'dashboard/services/list.html', {'services':services})

def create_service(request):
    if request.method == 'POST':
        icon = request.FILES['icon']
        title = request.POST['title']
        description = request.POST['description']
        models.Services.objects.create(
            icon=icon,
            title=title,
            description=description
        )
        return redirect('services')
    return render(request, 'dashboard/services/create.html', {'services':services})
    
def update_service(request, id):
    services = models.Services.objects.get(id=id)
    if request.method == 'POST':
        icon = request.FILES.get('icon')
        if icon:
            services.icon = request.FILES.get('icon')
        services.title = request.POST['title']
        services.description = request.POST['description']
        services.save()
        return redirect('services')
    return render(request, 'dashboard/services/update.html', {'services':services})
    
def delete_service(request, id):
    
    models.Services.objects.get(id=id).delete()
    return redirect('services')
    
# Clients
def clients(request):
    clients = models.Clients.objects.all()
    return render(request, 'dashboard/clients/list.html', {'clients':clients})

def create_client(request):
    if request.method =='POST':
        image = request.FILES.get('image')
        name = request.POST['name']
        opinion = request.POST['opinion']
        models.Clients.objects.create(
            image=image,
            name=name,
            opinion=opinion
        )
        return redirect('clients')
    return render(request, 'dashboard/clients/create.html')        

def update_client(request, id):
    client = models.Clients.objects.get(id=id)
    client.name = request.POST['name']
    client.opinion = request.POST['opinion']
    image = request.POST['image']
    if image:
        client.image = image
    client.save()

def delete_client(request, id):
    models.Clients.objects.get(id=id).delete()
    return redirect('clients') 

# Applications

def applications(request):
    applications = models.Contacts.objects.all()
    return render(request, 'dashboard/applications/list.html', {'applications':applications})

def read_application(request, id):
    application = models.Contacts.objects.get(id=id)
    is_read = request.POST['is_read']
    if is_read:
        application.is_read = is_read
    application.save()

# Authentication    
def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )

    return render(request, 'dashboard/auth/register.html')

def login(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )

    return render(request, 'dashboard/auth/login.html')


