# Generated by Django 4.1 on 2023-06-26 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inigramapp', '0006_alter_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
    ]
