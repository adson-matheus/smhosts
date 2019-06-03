set objSh = CreateObject("WScript.Shell")
objSh.Run "cmd /k CD %USERPROFILE% & CD ./ProjetosDjango/SMHosts/venv/Scripts & activate & CD %USERPROFILE% & CD ./ProjetosDjango/SMHosts/SMHosts/ & start http://localhost:80 & python manage.py runserver localhost:80", 0
MsgBox "SERVER INICIADO COM SUCESSO!"