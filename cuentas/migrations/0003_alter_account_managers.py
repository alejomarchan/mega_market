# Generated by Django 4.1.1 on 2022-10-08 19:19

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_rename_user_name_account_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
