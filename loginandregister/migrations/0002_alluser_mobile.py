# Generated by Django 3.2.5 on 2022-11-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginandregister', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alluser',
            name='mobile',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
