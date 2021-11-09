from .models import Host, Evento
from django.forms import ModelForm


class HostForm(ModelForm):
    class Meta:
        model = Host
        fields = '__all__'
        labels = {
            'hostname': ('HostName / IP'),
            'servico': ('Serviço'),
            'tipoHost': ('Tipo do Host'),
            'descricao': ('Descrição do Host'),
        }

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['host', 'status',]
