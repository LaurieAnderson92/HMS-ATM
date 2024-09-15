from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterList.as_view(), name='character-home'),
]
