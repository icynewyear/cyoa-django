# Generated by Django 3.2.4 on 2021-06-12 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20210611_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
