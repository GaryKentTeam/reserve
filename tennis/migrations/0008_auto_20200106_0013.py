# Generated by Django 2.2.5 on 2020-01-06 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0007_auto_20200106_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='court_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='failure_reason',
            field=models.CharField(default='', max_length=100),
        ),
    ]
