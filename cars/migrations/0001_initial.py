# Generated by Django 4.0.3 on 2022-03-15 11:59

import ckeditor.fields
import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('PA', 'Pennsylvania'), ('IL', 'Illinois'), ('DC', 'District Of Columbia'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('SC', 'South Carolina'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('CT', 'Connecticut'), ('NH', 'New Hampshire'), ('TX', 'Texas'), ('OK', 'Oklahoma'), ('ME', 'Maine'), ('KS', 'Kansas'), ('MN', 'Minnesota'), ('NC', 'North Carolina'), ('WA', 'Washington'), ('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('GA', 'Georgia'), ('NM', 'New Mexico'), ('MA', 'Massachusetts'), ('UT', 'Utah'), ('FL', 'Florida'), ('MT', 'Montana'), ('WV', 'West Virginia'), ('TN', 'Tennessee'), ('OR', 'Oregon'), ('MO', 'Missouri'), ('NV', 'Nevada'), ('NY', 'New York'), ('WY', 'Wyoming'), ('VT', 'Vermont'), ('CO', 'Colorado'), ('MI', 'Michigan'), ('HI', 'Hawaii'), ('WI', 'Wisconsin'), ('DE', 'Delaware'), ('MS', 'Mississippi'), ('MD', 'Maryland'), ('LA', 'Louisiana'), ('VA', 'Virginia'), ('KY', 'Kentucky'), ('OH', 'Ohio'), ('RI', 'Rhode Island'), ('CA', 'California'), ('AK', 'Alaska'), ('SD', 'South Dakota'), ('IN', 'Indiana'), ('NJ', 'New Jersey')], max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='year')),
                ('condition', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('car_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('features', multiselectfield.db.fields.MultiSelectField(choices=[('Seat Heating', 'Seat Heating'), ('ParkAssist', 'ParkAssist'), ('Airbags', 'Airbags'), ('Wind Deflector', 'Wind Deflector'), ('Air Conditioning', 'Air Conditioning'), ('Reversing Camera', 'Reversing Camera'), ('Cruise Control', 'Cruise Control'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Audio Interface', 'Audio Interface'), ('Alarm System', 'Alarm System'), ('Bluetooth Handset', 'Bluetooth Handset'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Power Steering', 'Power Steering')], max_length=195)),
                ('body_style', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=100)),
                ('interior', models.CharField(max_length=100)),
                ('miles', models.IntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('6', '6'), ('5', '5')], max_length=10)),
                ('passengers', models.IntegerField()),
                ('vin_no', models.CharField(max_length=100)),
                ('milage', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=50)),
                ('no_of_owners', models.CharField(max_length=100)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 15, 12, 59, 22, 40133))),
            ],
        ),
    ]