# Generated by Django 4.2.4 on 2023-09-07 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_rename_project_section_projectofsection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='projectOfSection',
        ),
    ]
