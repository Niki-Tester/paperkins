# Generated by Django 3.2.16 on 2022-10-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_query_type_contact_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='response_sent',
            field=models.BooleanField(default=False),
        ),
    ]
