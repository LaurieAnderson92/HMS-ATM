from django.shortcuts import render
from django.views import generic
from .models import Character

# ------------> Views

class CharacterList(generic.ListView):
    queryset = Character.objects.all()
    paginate_by = 3



def home(request):
    return render(request, 'character/home.html')


