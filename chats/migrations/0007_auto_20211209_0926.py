# Generated by Django 3.2.9 on 2021-12-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_auto_20211209_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='food',
            name='long',
        ),
        migrations.AddField(
            model_name='course',
            name='img_link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='img_link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='img_link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='img_link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='img_link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='long',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='img_link',
            field=models.TextField(null=True),
        ),
    ]
