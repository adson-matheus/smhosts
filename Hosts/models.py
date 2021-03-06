from django.db import models
from simple_history.models import HistoricalRecords

class Porta(models.Model):
    portaServico = models.IntegerField(blank=False, default=1)
    servico = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return '{}'.format(self.portaServico)

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
    tipoHost = models.CharField(
        max_length=20,
        choices=TIPO_HOST,
    )
    descricao = models.CharField(
        max_length=200,
        blank=True,
    )
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.hostname

class Host_Porta(models.Model):
    host = models.ForeignKey(Host, related_name='host', on_delete=models.CASCADE)
    porta = models.ForeignKey(Porta, related_name='porta', on_delete=models.CASCADE)

    class Meta:
        ordering = ('porta',)
    def __str__(self):
        return '{}:{}'.format(self.host, self.porta)

# 1 evento associado a 1 host
class Evento(models.Model):
    STATUS = (
        ('ONLINE', 'ONLINE'),
        ('OFFLINE', 'OFFLINE'),
        ('DEMORANDO', 'DEMORANDO'),
    )
    dataHora = models.DateTimeField(
        auto_now=True,
        blank=False,
    )
    status = models.TextField(
        choices=STATUS,
        blank=True,
        default = ''
    )
    ping = models.FloatField(
        blank=True,
        null=True,
        max_length=50)
    host_porta_id = models.ForeignKey(
        Host_Porta,
        null=True,
        related_name='host_porta_id',
        on_delete=models.CASCADE
    )
    history = HistoricalRecords(cascade_delete_history=True)
    def __str__(self):
        return '{} - {}'.format(self.host_porta_id, self.status)