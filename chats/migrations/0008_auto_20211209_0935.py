# Generated by Django 3.2.9 on 2021-12-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0007_auto_20211209_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='locationtype',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
    ]