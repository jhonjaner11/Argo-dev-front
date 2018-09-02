from django import forms
from dependences.models import Dependence

class DependenceForm(forms.ModelForm):
    class Meta:
        model= Dependence
        fields=[
               'code',
               'initials',
               'name',
               'parent',
               ]
        labels={
                'code':'Código',
                'initials': 'Sigla',
                'name':'Nombre',
                'parent':'Dependencia padre',
                }


                
