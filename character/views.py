from django.shortcuts import render
from django.views import generic
from .models import Character, Account

# ------------> Views

def home(request):
    characters = Character.objects.all()  # Get all characters initially
    accounts = Account.objects.all()  # Get all accounts

    if request.user.is_authenticated:
        # Filter characters for authenticated users
        characters = characters.filter(player=request.user)
        accounts = accounts.filter(owner__in=characters)
    else:
        # Empty queryset for anonymous users
        characters = characters.none()
        accounts = accounts.none()
    return render(
        request, 
        'character/account_list.html', 
        {
            'characters': characters,
            'accounts': accounts
            
        }
    )


