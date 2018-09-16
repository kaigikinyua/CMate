from django.db import models
from datetime import datetime
from django.core.files.storage import FileSystemStorage
# Create your models here.
class Profile(models.Model):
    profile=models.ImageField()
    useremail=models.EmailField()
    def __str__(self):
        return self.useremail
class UserDetails(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.username+" - "+self.email+" - "+self.password
class ChatStats(models.Model):
    Topic=models.CharField(max_length=50)
    Number=models.IntegerField(default=0)
    Publicity=models.BooleanField(default=True)
    Admin=models.CharField(max_length=30)
    def __str__(self):
        return self.Topic+" - "+self.Number
class Chats(models.Model):
    Sender=models.CharField(max_length=50)
    Receiver=models.CharField(max_length=50)
    Message=models.CharField(max_length=250)
    Time=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.Sender+' - '+self.Receiver+' - '+self.Message+' - '+self.Time
