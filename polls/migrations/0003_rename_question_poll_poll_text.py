# Generated by Django 5.0 on 2024-01-06 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_poll_pollchoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='question',
            new_name='poll_text',
        ),
    ]