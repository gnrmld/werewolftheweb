from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import Player
from .forms import PlayerForm

# Create your views here.
def is_not_signed_up(request):
    visitor_ip = request.META.get('REMOTE_ADDR')
    try:
        player = Player.objects.get(pk=visitor_ip)
        return False
    except ObjectDoesNotExist:
        return True

def create(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.pk = request.META.get('REMOTE_ADDR')
            player.save()
            return redirect('/')
    else:
        form = PlayerForm()
    context = {
        'form' : form,
    }
    return render(request, 'player/create.html', context)