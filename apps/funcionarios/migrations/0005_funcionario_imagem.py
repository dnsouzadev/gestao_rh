# Generated by Django 5.0.6 on 2024-05-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_alter_funcionario_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='funcionarios'),
        ),
    ]
