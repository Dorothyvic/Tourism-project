# Generated by Django 2.2 on 2020-09-23 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('message', models.TextField()),
            ],
        ),
    ]
