from django.urls import path
from .views  import index, contact, service, about

urlpatterns = [
    path('', index, name = 'index'),
    path('contact/', contact, name = 'contact'),
    path('service/', service, name = 'service'),
    path('about/', about, name = 'about'),
]