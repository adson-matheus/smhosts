from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Principal:principal')
    else:
        form = UserCreationForm()
    return render(request, 'cadastroUsuario/signup.html', {'form':form})