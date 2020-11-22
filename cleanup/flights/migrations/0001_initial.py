# Generated by Django 3.1.2 on 2020-10-24 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testFlightData',
            fields=[
                ('flightNum', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('origin', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('flightDateTime', models.DateTimeField()),
                ('flightCost', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
