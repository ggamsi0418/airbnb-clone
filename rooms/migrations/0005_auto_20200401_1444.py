# Generated by Django 2.2.5 on 2020-04-01 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200328_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='roo_type',
            new_name='room_type',
        ),
    ]
