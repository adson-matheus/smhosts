from .models import Evento, Host_Porta
from django.forms import ModelForm


class Host_PortaForm(ModelForm):
    class Meta:
        model = Host_Porta
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
        fields = ['status',]
