# Generated by Django 4.1.3 on 2023-03-18 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liveproapp', '0003_contact_tb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_tb',
            old_name='message',
            new_name='cn_message',
        ),
    ]
