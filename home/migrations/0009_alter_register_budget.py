# Generated by Django 5.1.3 on 2025-01-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_register_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='budget',
            field=models.CharField(max_length=122),
        ),
    ]
