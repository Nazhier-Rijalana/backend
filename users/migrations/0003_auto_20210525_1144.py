# Generated by Django 3.2.3 on 2021-05-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_date_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type_user',
        ),
        migrations.AddField(
            model_name='user',
            name='phase',
            field=models.IntegerField(choices=[(0, 'KEHAMILAN'), (1, 'AWAL MENYUSUI'), (2, 'MPASI')], default=0),
        ),
    ]
