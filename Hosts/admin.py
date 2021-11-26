from django.contrib import admin
from .models import Host, Evento, Porta, Host_Porta
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Host)
#admin.site.register(Evento)
admin.site.register(Porta)
admin.site.register(Host_Porta)
admin.site.register(Evento, SimpleHistoryAdmin)
