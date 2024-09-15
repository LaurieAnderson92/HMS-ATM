# Generated by Django 5.1.1 on 2024-09-15 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('value', models.IntegerField(default=0)),
                ('is_guild_account', models.BooleanField(default=False)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_frozen', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
