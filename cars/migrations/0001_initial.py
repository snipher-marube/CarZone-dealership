# Generated by Django 5.0.6 on 2024-07-06 15:05

import ckeditor_uploader.fields
import datetime
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('Meru', 'Meru'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Kisii', 'Kisii'), ('Machakos', 'Machakos'), ('Nairobi', 'Nairobi'), ('Garissa', 'Garissa'), ('Nyamira', 'Nyamira'), ('Kericho', 'Kericho'), ('Embu', 'Embu'), ('Naivasha', 'Naivasha'), ('Nakuru', 'Nakuru'), ('Namanga', 'Namanga'), ('Migori', 'Migori'), ('Kakamega', 'Kakamega'), ('Eldoret', 'Eldoret'), ('Bungoma', 'Bungoma'), ('Kwale', 'Kwale'), ('Limuru', 'Limuru'), ('Kolgoris', 'Kilgoris'), ('Kitengela', 'Kitengela'), ('Karen', 'Karen'), ('Lavington', 'Lavington'), ('Nyeri', 'Nyeri'), ('Mwea', 'Mwea'), ('Homa Bay', 'Homa Bay'), ('Ogembo', 'Ogembo'), ('Siaya', 'Siaya'), ('Kilifi', 'Kilifi'), ('Malindi', 'Malindi'), ('Namanga', 'Namanga')], max_length=9)),
                ('color', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], verbose_name='year')),
                ('condition', models.CharField(choices=[('Used', 'Used'), ('New', 'New'), ('Refurbished', 'Refurbished')], max_length=12)),
                ('price', models.IntegerField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('car_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('features', multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=255)),
                ('body_style', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual'), ('Automated Manual', 'Automated Manual'), ('Continuos Variable', 'Continuosly Variable')], max_length=18)),
                ('interior', models.CharField(max_length=100)),
                ('miles', models.IntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10)),
                ('passengers', models.IntegerField()),
                ('vin_no', models.CharField(max_length=100)),
                ('milage', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=50)),
                ('no_of_owners', models.CharField(max_length=100)),
                ('tag', models.CharField(blank=True, choices=[('FOR RENT', 'FOR RENT'), ('FOR HIRE', 'FOR HIRE'), ('FOR SALE', 'FOR SALE')], max_length=9, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
