# Generated by Django 2.1.5 on 2020-02-13 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0013_auto_20200213_0332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policy',
            old_name='Title',
            new_name='Program',
        ),
    ]
