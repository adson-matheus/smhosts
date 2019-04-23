from .models import Hosts
from django import forms
from django.forms import ModelForm


class HostForm(ModelForm):
    class Meta:
        model = Hosts
        fields = '__all__'
        labels = {
            'hostname': ('HostName / IP'),
            'porta': ('Porta'),
            'tipoHost': ('Tipo do Host'),
            'descricao': ('Descrição do Host')
        }
