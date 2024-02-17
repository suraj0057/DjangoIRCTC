# Generated by Django 5.0.1 on 2024-02-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.BigIntegerField()),
                ('pass_name', models.CharField(max_length=100)),
                ('pass_age', models.BigIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('seat_no', models.BigIntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainNo', models.BigIntegerField()),
                ('trainName', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('arrivalTime', models.TimeField(default='00:00:00')),
                ('departureTime', models.TimeField(default='00:00:00')),
                ('sleeperAvailable', models.BigIntegerField(default=0)),
                ('sleeperWaiting', models.BigIntegerField(default=0)),
                ('acAvailable', models.BigIntegerField(default=0)),
                ('acWaiting', models.BigIntegerField(default=0)),
            ],
        ),
    ]
