from django.db import models
from dependences.models import Dependence
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, blank=True, null=True)
    document_number = models.IntegerField(unique=True)
    def get_complete_name(self):
        return self.first_name+" "+self.last_name

class ArgoUser(models.Model):
    #state = models.CharField(max_length=15, choices=STATES, default='ACTIVE')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    dependence = models.ForeignKey(Dependence, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        
