# Generated by Django 3.2.15 on 2022-10-06 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_profile_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TutorialPost',
            new_name='TeamPost',
        ),
    ]