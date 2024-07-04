from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField


class Car(models.Model):
    STATE_CHOICES = (
        ('MU', 'Meru'),
        ('MA', 'Mombasa'),
        ('KU', 'Kisumu'),
        ('KI', 'Kisii'),
        ('MS', 'Machakos'),
        ('NI', 'Nairobi'),
        ('GA', 'Garissa'),
        ('NA', 'Nyamira'),
        ('KO', 'Kericho'),
        ('EM', 'Embu'),
        ('NV', 'Naivasha'),
        ('NK', 'Nakuru'),
        ('NM', 'Namanga'),
        ('MI', 'Migori'),
        ('KG', 'Kakamega'),
        ('EL', 'Eldoret'),
        ('BM', 'Bungoma'),
        ('KL', 'Kwale'),
        ('LM', 'Limuru'),
        ('KR', 'Kilgoris'),
        ('KT', 'Kitengela'),
        ('KN', 'Karen'),
        ('LV', 'Lavington'),
        ('NR', 'Nyeri'),
        ('MA', 'Mwea'),
        ('HB', 'Homa Bay'),
        ('OG', 'Ogembo'),
        ('SY', 'Siaya'),
        ('KF', 'Kilifi'),
        ('MD', 'Malindi'),
        ('NG', 'Namanga'),
        ('NM', 'New Mexico'),

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
        ('AT', 'Automatic'),
        ('MT', 'Manual'),
        ('AM', 'Automated Manual'),
        ('CVT', 'Continuosly Variable'),
    )
    CAR_CONDITION = (
        ('u', 'Used'),
        ('n', 'New'),
        ('r', 'Refurbished'),
    )

    car_title = models.CharField(max_length=100)
    state = models.CharField(choices=STATE_CHOICES, max_length=2)
    color = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=YEAR_CHOICE)
    condition = models.CharField(choices=CAR_CONDITION, max_length=1)
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
    transmission = models.CharField(choices=TRANSMISSION_MODES, max_length=3)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=DOOR_CHOICES, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['-created_date']  # order by latest

    def __str__(self):
        return self.car_title
