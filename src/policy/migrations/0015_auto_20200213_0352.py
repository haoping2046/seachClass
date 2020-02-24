# Generated by Django 2.1.5 on 2020-02-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0014_auto_20200213_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policy',
            name='year_in_school',
        ),
        migrations.AlterField(
            model_name='policy',
            name='Program',
            field=models.CharField(choices=[('MS', 'M.S.'), ('MEng', 'M.Eng.'), ('PhD', 'Ph.D.')], default='MS', max_length=2),
        ),
    ]