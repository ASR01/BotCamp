# Generated by Django 3.2.9 on 2021-12-09 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0011_alter_locationtype_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationtype',
            name='created',
        ),
        migrations.RemoveField(
            model_name='locationtype',
            name='updated',
        ),
    ]
