# Generated by Django 2.1.5 on 2020-02-13 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0004_auto_20200212_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policy',
            name='MEng',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='MS',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='PhD',
        ),
    ]
