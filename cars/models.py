from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField


class Car(models.Model):
    STATE_CHOICES = (
        ('Meru', 'Meru'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
        ('Kisii', 'Kisii'),
        ('Machakos', 'Machakos'),
        ('Nairobi', 'Nairobi'),
        ('Garissa', 'Garissa'),
        ('Nyamira', 'Nyamira'),
        ('Kericho', 'Kericho'),
        ('Embu', 'Embu'),
        ('Naivasha', 'Naivasha'),
        ('Nakuru', 'Nakuru'),
        ('Namanga', 'Namanga'),
        ('Migori', 'Migori'),
        ('Kakamega', 'Kakamega'),
        ('Eldoret', 'Eldoret'),
        ('Bungoma', 'Bungoma'),
        ('Kwale', 'Kwale'),
        ('Limuru', 'Limuru'),
        ('Kolgoris', 'Kilgoris'),
        ('Kitengela', 'Kitengela'),
        ('Karen', 'Karen'),
        ('Lavington', 'Lavington'),
        ('Nyeri', 'Nyeri'),
        ('Mwea', 'Mwea'),
        ('Homa Bay', 'Homa Bay'),
        ('Ogembo', 'Ogembo'),
        ('Siaya', 'Siaya'),
        ('Kilifi', 'Kilifi'),
        ('Malindi', 'Malindi'),
        ('Namanga', 'Namanga'),

    )

    YEAR_CHOICE = []
    for year in range(2000, (datetime.now().year+1)):
        YEAR_CHOICE.append((year, year))

    FEATURES_CHOICES = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    DOOR_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    TRANSMISSION_MODES = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
        ('Automated Manual', 'Automated Manual'),
        ('Continuos Variable', 'Continuosly Variable'),
    )
    CAR_CONDITION = (
        ('Used', 'Used'),
        ('New', 'New'),
        ('Refurbished', 'Refurbished'),
    )

    TAGS = (
        ('FOR RENT', 'FOR RENT'),
        ('FOR HIRE', 'FOR HIRE'),
        ('FOR SALE', 'FOR SALE')
    )
    
    car_title = models.CharField(max_length=100)
    state = models.CharField(choices=STATE_CHOICES, max_length=9)
    color = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=YEAR_CHOICE)
    condition = models.CharField(choices=CAR_CONDITION, max_length=12)
    price = models.IntegerField()
    description = RichTextUploadingField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=FEATURES_CHOICES, max_length=255)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(choices=TRANSMISSION_MODES, max_length=18)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=DOOR_CHOICES, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    tag = models.CharField(choices=TAGS, max_length=9, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['-created_date']  # order by latest

    def __str__(self):
        return self.car_title
