# Generated by Django 4.1 on 2022-08-14 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_projects_alter_userprojects_project_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='projects',
        ),
        migrations.DeleteModel(
            name='UserProjects',
        ),
    ]