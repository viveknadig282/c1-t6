# Generated by Django 3.2.8 on 2021-11-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0015_alter_ingredient_within_food'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='ingredient_content',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='within_food',
            new_name='foods',
        ),
    ]