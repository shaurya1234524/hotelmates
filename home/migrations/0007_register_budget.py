# Generated by Django 5.1.3 on 2024-12-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_register_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='budget',
            field=models.TextField(default='datetime'),
        ),
    ]
