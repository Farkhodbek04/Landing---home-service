from django.db import models
class Services(models.Model):
    icon = models.ImageField(upload_to='services')
    title = models.CharField(max_length=35)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
class Clients(models.Model):
    image = models.ImageField(upload_to='clients')
    name = models.CharField(max_length=20)
    opinion = models.CharField(max_length=255)

    def __str__(self)-> str:
        return self.name
    
class Contacts(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


# Create your models here.
