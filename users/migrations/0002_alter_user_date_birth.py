# Generated by Django 3.2.3 on 2021-05-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_birth',
            field=models.DateField(null=True),
        ),
    ]
