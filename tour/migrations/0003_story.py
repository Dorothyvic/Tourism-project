# Generated by Django 2.2 on 2020-09-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_auto_20200921_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='1.jpg', null=True, upload_to='')),
                ('header', models.CharField(max_length=100)),
                ('paragraph', models.TextField()),
            ],
        ),
    ]
