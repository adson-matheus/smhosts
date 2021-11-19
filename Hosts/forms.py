from .models import Evento, Host_Porta, Host
from django.forms import ModelForm


class Host_PortaForm(ModelForm):
    class Meta:
        model = Host_Porta
        fields = '__all__'
        labels = {
            'hostname': ('HostName / IP'),
            'tipoHost': ('Tipo do Host'),
            'descricao': ('Descrição do Host'),
        }

class HostForm(ModelForm):
    class Meta:
        model = Host
        fields = ['hostname', 'tipoHost', 'descricao']

