# Generated by Django 5.0.5 on 2024-05-09 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_alter_documento_pertence'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentos'),
            preserve_default=False,
        ),
    ]
