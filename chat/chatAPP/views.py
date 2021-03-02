from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
from chatAPP.models import Room
from django.urls import reverse


@login_required
def main(request):
    return HttpResponse("Main page")


@login_required
def index(request):
    return render(request, 'chat/index.html')


@login_required
def room(request, room_id):
    room_obj = get_object_or_404(Room, id=room_id)
    try:
        request.user.rooms.get(id=room_id)
        return render(request, 'chat/room.html', {
            'room_name': room_obj.id
        })
    except ObjectDoesNotExist:
        return HttpResponse('You have no access to this chat')


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