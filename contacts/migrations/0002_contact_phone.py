# Generated by Django 4.0.4 on 2022-05-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
