from Hosts.models import Porta
from django.forms import ModelForm

class PortaForm(ModelForm):
    class Meta:
        model = Porta
        fields = ['portaServico', 'servico']