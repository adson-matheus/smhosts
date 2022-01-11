# SMHosts
Sistema de Monitoramento de Hosts

Este projeto serve para monitorar os hosts dentro de uma rede, sua principal função é identificar hosts offline e os que estão com um ping muito alto, por exemplo.

O monitoramento é feito por meio de uma função que utiliza o <a href="https://pypi.org/project/ping3/" target="_blank">ping3</a> do Python.

O projeto utiliza <a href="https://www.djangoproject.com/" target="_blank">Django</a> para funcionar na Web, e para os gráficos foi utilizado o <a href="https://www.zingchart.com/" target="_blank">ZingChart Javascript</a> e a biblioteca <a href="https://django-simple-history.readthedocs.io/en/latest/" target="_blank">Django Simple Story</a>, que salva as alterações de status e os respectivos pings ao longo do tempo.
