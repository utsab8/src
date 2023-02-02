from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract =True
        
        
class Home(TimeStampModel):
    name = models.CharField(max_length=20)
    greeting_1 = models.CharField(max_length=20)
    about = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
class About(TimeStampModel):
    heading = models.CharField(max_length=50)
    carrer = models.CharField(max_length=355)
    image = models.ImageField(upload_to='about/')
    
    def __Str__(self):
        return self.carrer
    
    
class Service(TimeStampModel):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
    
class Portfolio(TimeStampModel):
    name = models.CharField(max_length=55)
    about = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return f'portfolio {self.id}'
    
    
class Contact(TimeStampModel):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  number = models.IntegerField()
  message = models.TextField()