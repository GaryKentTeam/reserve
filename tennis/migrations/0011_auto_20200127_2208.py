# Generated by Django 2.2.5 on 2020-01-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0010_booking_confirmation_screenshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='confirmation_screenshot',
        ),
        migrations.AddField(
            model_name='booking',
            name='confirmation_screenshot_path',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
