# Generated by Django 4.0.3 on 2022-03-28 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_response_user_note_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='user_fio',
        ),
    ]
