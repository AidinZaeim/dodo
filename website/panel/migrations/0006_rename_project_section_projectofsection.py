# Generated by Django 4.2.4 on 2023-09-07 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_remove_project_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='project',
            new_name='projectOfSection',
        ),
    ]
