# Generated by Django 5.1.3 on 2025-01-04 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='myphone',
            new_name='phone',
        ),
    ]