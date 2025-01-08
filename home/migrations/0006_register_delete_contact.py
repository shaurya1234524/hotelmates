# Generated by Django 5.1.3 on 2024-12-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='REGISTER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotel', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('checkindate', models.TextField()),
                ('checkoutdate', models.TextField()),
                ('username', models.CharField(default='datetime', max_length=122)),
                ('messsage', models.CharField(default='datetime', max_length=122)),
                ('phone', models.CharField(default='No Phone number mentioned', max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
