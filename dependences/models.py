from django.db import models

# Create your models here.

class Dependence(models.Model):
    code = models.CharField(max_length=10,unique=True)
    initials = models.CharField(max_length=5,unique=True)
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def get_name(self):
        return self.name
