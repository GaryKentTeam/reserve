# Generated by Django 2.2.5 on 2020-01-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courtlocation',
            name='name',
            field=models.CharField(default='Alice Marbles', max_length=1000, unique=True),
        ),
    ]
