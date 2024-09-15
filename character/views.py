from django.shortcuts import render
from django.views import generic
from .models import Character

# ------------> Views

def home(request):
    characters = Character.objects.all()  # Get all characters initially

    if request.user.is_authenticated:
        # Filter characters for authenticated users
        characters = characters.filter(player=request.user)
    else:
        # Empty queryset for anonymous users
        characters = characters.none()
    return render(request, 'character/account_list.html', {'characters': characters})


