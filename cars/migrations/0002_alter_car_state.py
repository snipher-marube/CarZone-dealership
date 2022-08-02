# Generated by Django 4.0.6 on 2022-08-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('MU', 'Meru'), ('MA', 'Mombasa'), ('KU', 'Kisumu'), ('KI', 'Kisii'), ('MS', 'Machakos'), ('NI', 'Nairobi'), ('GA', 'Garissa'), ('NA', 'Nyamira'), ('KO', 'Kericho'), ('EM', 'Embu'), ('NV', 'Naivasha'), ('NK', 'Nakuru'), ('NM', 'Namanga'), ('MI', 'Migori'), ('KG', 'Kakamega'), ('EL', 'Eldoret'), ('BM', 'Bungoma'), ('KL', 'Kwale'), ('LM', 'Limuru'), ('KR', 'Kilgoris'), ('KT', 'Kitengela'), ('KN', 'Karen'), ('LV', 'Lavington'), ('NR', 'Nyeri'), ('MA', 'Mwea'), ('HB', 'Homa Bay'), ('OG', 'Ogembo'), ('SY', 'Siaya'), ('KF', 'Kilifi'), ('MD', 'Malindi'), ('NG', 'Namanga'), ('NM', 'New Mexico')], max_length=2),
        ),
    ]
