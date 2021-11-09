from django.db import models

#from Principal.views import verificaServer

# Create your models here.
class Host(models.Model):
    TIPO_HOST = (
        ('Access Point', 'ACCESS POINT'),
        ('Desktop', 'DESKTOP'),
        ('Impressora', 'IMPRESSORA'),
        ('Notebook', 'NOTEBOOK'),
        ('Servidor', 'SERVIDOR'),
        ('Outros', 'OUTROS'),
    )
    hostname = models.CharField(
        max_length=100,
        blank=False
    )
    servico = models.CharField(
        max_length=100,
        blank=False,
        default='',
    )
    tipoHost = models.CharField(
        max_length=20,
        choices=TIPO_HOST,
    )
    descricao = models.CharField(
        max_length=200,
        blank=True
    )
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.hostname


class Evento(models.Model):
    STATUS = (
        ('ONLINE', 'ONLINE'),
        ('OFFLINE', 'OFFLINE'),
        ('DEMORANDO', 'DEMORANDO'),
    )
    host = models.ForeignKey(Host,
        related_name="host",
        on_delete=models.CASCADE,
        blank=True)

    dataHora = models.DateTimeField(
        auto_now=True,
        blank=True,
    )
    status = models.TextField(
        choices=STATUS,
        blank=True,
        default = ''
    )
    def __str__(self):
        return '{} - Status: {}' .format(self.host.hostname, self.status)

class Servico(models.Model):
    porta = models.ForeignKey(Host, related_name='portas', on_delete=models.CASCADE, blank=True)
    
