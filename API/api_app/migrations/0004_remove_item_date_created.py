# Generated by Django 3.2.15 on 2023-05-17 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_alter_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='date_created',
        ),
    ]