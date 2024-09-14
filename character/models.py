from django.db import models
from django.contrib.auth.models import User

CHARACTER_STATUS = ((0, "Draft"), (1, "Active"))

# Create your models here.
class Character(models.Model):
    name = models.CharField()
    body = models.TextField()
    player = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='character', null=True)
    status = models.IntegerField(choices=CHARACTER_STATUS, default=0)
    is_npc = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({user.username})"
    