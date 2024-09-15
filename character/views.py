from django.shortcuts import render
from django.views import generic
from .models import Character

# ------------> Views


def home(request):
    return render(request, 'character/account_list.html')


