from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Role

# Create your views here.
def list(request):
    roles = Role.objects.all().order_by('character_priority')
    context = {
        'roles': roles,
    }
    return render(request, 'characters/list.html', context)