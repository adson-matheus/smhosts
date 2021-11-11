from django.db import models


class Evento(models.Model):
    STATUS = (
        ('ONLINE', 'ONLINE'),
        ('OFFLINE', 'OFFLINE'),
        ('DEMORANDO', 'DEMORANDO'),
    )
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
        return '{}'.format(self.status)

class Porta(models.Model):
    portaServico = models.IntegerField(primary_key=True, blank=False)
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
    #evento = models.ForeignKey(Evento, related_name='evento', on_delete=models.CASCADE)

    class Meta:
        ordering = ('porta',)
    def __str__(self):
        return '{}:{}'.format(self.host, self.porta)