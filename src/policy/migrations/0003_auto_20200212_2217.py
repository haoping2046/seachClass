# Generated by Django 2.1.5 on 2020-02-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0002_auto_20200212_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
