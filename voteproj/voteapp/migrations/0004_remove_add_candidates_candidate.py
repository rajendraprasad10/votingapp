# Generated by Django 3.1.4 on 2020-12-08 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0003_remove_like_condidate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_candidates',
            name='candidate',
        ),
    ]