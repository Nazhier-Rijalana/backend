# Generated by Django 3.2.3 on 2021-05-25 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awal_menyusui', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menyusui',
            old_name='name',
            new_name='baby_name',
        ),
        migrations.RemoveField(
            model_name='menyusui',
            name='type',
        ),
    ]
