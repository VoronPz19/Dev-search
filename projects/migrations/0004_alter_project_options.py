# Generated by Django 4.2.4 on 2023-09-12 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', '-created']},
        ),
    ]
