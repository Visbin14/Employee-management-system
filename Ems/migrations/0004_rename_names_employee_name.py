# Generated by Django 4.1.3 on 2022-11-03 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ems', '0003_alter_log_status_log'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='names',
            new_name='name',
        ),
    ]
