# Generated by Django 4.2.4 on 2023-09-07 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
    ]
