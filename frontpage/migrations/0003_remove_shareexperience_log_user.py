# Generated by Django 3.2.8 on 2021-10-14 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_donorregister_today_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shareexperience',
            name='log_user',
        ),
    ]