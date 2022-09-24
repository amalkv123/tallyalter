# Generated by Django 4.0.5 on 2022-07-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rounding_gratuity_compute_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='gst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=225)),
                ('type', models.CharField(max_length=225)),
                ('teretory', models.CharField(max_length=225)),
                ('uin', models.CharField(max_length=225)),
                ('gstr1', models.CharField(max_length=225)),
                ('kerala', models.CharField(max_length=225)),
                ('set', models.CharField(max_length=225)),
                ('enable', models.CharField(max_length=225)),
                ('enable2', models.CharField(max_length=225)),
                ('enable3', models.CharField(max_length=225)),
                ('bond', models.CharField(max_length=225)),
                ('taxrate', models.CharField(max_length=225)),
                ('basistax', models.CharField(max_length=225)),
                ('purchase', models.CharField(max_length=225)),
                ('eway', models.CharField(max_length=225)),
                ('applicable', models.CharField(max_length=225)),
                ('thresholt', models.CharField(max_length=225)),
                ('limit', models.CharField(max_length=225)),
                ('infrastate', models.CharField(max_length=225)),
                ('thresholt2', models.CharField(max_length=225)),
                ('invoice', models.CharField(max_length=225)),
                ('einvoice', models.CharField(max_length=225)),
            ],
        ),
    ]