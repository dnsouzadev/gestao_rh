# Generated by Django 5.0.6 on 2024-05-22 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0002_registrohoraextra_horas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='utilizada',
            field=models.BooleanField(default=False),
        ),
    ]
