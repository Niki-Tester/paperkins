# Generated by Django 3.2.16 on 2022-10-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20221010_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]