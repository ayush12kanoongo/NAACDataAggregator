# Generated by Django 3.2.5 on 2022-11-17 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0002_collaborative_activity'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_collaborative_activity_participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.collaborative_activity')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
