from django.urls import path
from .views  import  (index, contact, service, about, dashboard, services, create_service, update_service, delete_service, clients, create_client, update_client, delete_client, applications, read_application, register, login )

urlpatterns = [
    # front
    path('', index, name = 'index'),
    path('contact/', contact, name = 'contact'),
    path('service/', service, name = 'service'),
    path('about/', about, name = 'about'),
    # dashboard
    path('dashboard/', dashboard, name = 'dashboard'),
    # service
    path('dashboard/services/list', services,  name = 'services'),
    path('dashboard/services/create', create_service,  name = 'create_service'),
    path('dashboard/services/update/<int:id>', update_service,  name = 'update_service'),
    path('dashboard/services/delete/<int:id>', delete_service,  name = 'delete_service'),
    # clients
    path('dashboard/clients/list', clients,  name = 'clients'),
    path('dashboard/clients/create', create_client,  name = 'create_client'),
    path('dashboard/clients/update/<int:id>', update_client,  name = 'update_client'),
    path('dashboard/clients/delete/<int:id>', delete_client,  name = 'delete_client'),
    # appliacations
    path('dashboard/applications/list', applications,  name = 'applications'),
    path('dashboard/applications/read/<int:id>', read_application,  name = 'read_application'),
    # authentication
    path('dashboard/auth/register', register, name = 'register'),
    path('dashboard/auth/login', login, name = 'login'),

    

]