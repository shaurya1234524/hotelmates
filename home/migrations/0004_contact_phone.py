# Generated by Django 5.1.3 on 2024-11-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_messsage_contact_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='datetime', max_length=12),
        ),
    ]
