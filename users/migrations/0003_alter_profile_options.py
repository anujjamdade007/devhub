# Generated by Django 5.0.4 on 2024-05-15 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]