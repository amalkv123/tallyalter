# Generated by Django 4.0.5 on 2022-09-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_createemployeegrp_remove_employee_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='units',
            name='uqc1',
            field=models.CharField(blank=True, default='null', max_length=225),
        ),
    ]