# Generated by Django 3.2.9 on 2021-12-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0014_auto_20211209_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='brief_desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='body',
            field=models.CharField(max_length=200),
        ),
    ]
