# Generated by Django 2.1 on 2021-07-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='subject_musics/', verbose_name='Ajouter fichier (optionnel)'),
        ),
    ]
