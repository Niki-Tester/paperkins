# Generated by Django 3.2.16 on 2022-10-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_response_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='response_message',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
