# Generated by Django 4.2.2 on 2023-07-31 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_alter_movement_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.IntegerField(max_length=50),
        ),
    ]
