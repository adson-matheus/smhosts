set objSh = CreateObject("WScript.Shell")

objSh.Run "cmd /k CD %USERPROFILE% & CD ./ProjetosDjango/SMHosts/venv/Scripts & activate & CD %USERPROFILE% & CD ./ProjetosDjango/SMHosts/SMHosts/ & start http://localhost:81 & python manage.py runserver localhost:81", 1

WScript.Sleep 5000

MsgBox "INICIANDO O SERVIDOR... EM ALGUNS SEGUNDOS, ATUALIZE A PAGINA DO SISTEMA NO SEU NAVEGADOR!"