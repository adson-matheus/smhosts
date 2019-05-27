from django.db import models

# Create your models here.
class Hosts(models.Model):
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
    porta = models.PositiveIntegerField(
        default=0,
        blank=False
    )
    tipoHost = models.CharField(
        max_length=20,
        choices=TIPO_HOST,
        default=''
    )
    descricao = models.CharField(
        max_length=200,
        blank=False
    )
    status = models.BooleanField(
        default=False
    )
    
    def __str__(self):
        return self.hostname
    
