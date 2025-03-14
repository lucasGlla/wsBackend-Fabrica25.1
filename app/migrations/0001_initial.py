# Generated by Django 5.1.6 on 2025-03-01 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeUsuario', models.CharField(max_length=255)),
                ('emailUsuario', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AvatarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatarUrl', models.URLField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Avatares', to='app.usuariomodel')),
            ],
        ),
    ]
