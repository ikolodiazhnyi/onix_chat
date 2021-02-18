from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def index(request):
    return render(request, 'chat/index.html')


@login_required()
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/chat/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})