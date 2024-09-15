# Generated by Django 5.1.1 on 2024-09-15 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accounts', to='character.character'),
        ),
    ]
