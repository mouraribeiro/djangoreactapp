# Generated by Django 3.0 on 2024-01-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]