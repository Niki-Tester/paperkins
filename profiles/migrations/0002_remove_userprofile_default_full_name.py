# Generated by Django 3.2.16 on 2022-10-05 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_full_name',
        ),
    ]