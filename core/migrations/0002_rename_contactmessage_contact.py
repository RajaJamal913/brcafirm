# Generated by Django 5.0.6 on 2024-09-10 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactMessage',
            new_name='Contact',
        ),
    ]
