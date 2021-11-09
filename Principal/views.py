from django.shortcuts import render
from urllib import request
from django.contrib.auth.decorators import login_required
from Hosts.models import Host
from Hosts.views import verificaServer

import json

@login_required
def principal(request):
    hosts = Host.objects.all()
    return render(request, 'principal.html', {'hosts': hosts})