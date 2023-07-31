# Generated by Django 4.2.2 on 2023-07-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_card_remove_visitor_date_remove_visitor_devices_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaitingList',
            fields=[
                ('id_passport_nbr', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('country_of_origin', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('mobile_phone', models.CharField(max_length=20)),
            ],
        ),
    ]