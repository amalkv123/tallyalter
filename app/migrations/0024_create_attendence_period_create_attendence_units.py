# Generated by Django 4.0.5 on 2022-09-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_companies_unitquantitycode'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_attendence',
            name='period',
            field=models.CharField(blank=True, default='null', max_length=225),
        ),
        migrations.AddField(
            model_name='create_attendence',
            name='units',
            field=models.CharField(blank=True, default='null', max_length=225),
        ),
    ]
