# Generated by Django 2.2 on 2020-09-21 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='pirce',
            new_name='price',
        ),
    ]