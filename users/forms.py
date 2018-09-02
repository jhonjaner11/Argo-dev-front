from django import forms
from users.models import Person, ArgoUser

class PersonForm(forms.ModelForm):
    class Meta:
        model= Person
        fields=[
               'first_name',
               'last_name',
               'email',
               'document_number',
               ]
        labels={
                'first_name':'Nombres',
                'last_name': 'Apellido',
                'email':'Correo electrónico',
                'document_number':'Número de documento',
                }
class ArgoUserForm(forms.ModelForm):
    class Meta:
        model=ArgoUser 
        fields=[
               'person',
               'dependence',
               'user',
               ]
        labels={
                'person':'Persona',
                'dependence': 'Dependencia',
                'usuario':'Usuario',
                }
