from django.db import models

# Create your models here.

class Train(models.Model):
       trainNo=models.BigIntegerField()
       trainName=models.CharField(max_length=100)
       source=models.CharField(max_length=100)
       destination=models.CharField(max_length=100)
       arrivalTime=models.TimeField(default='00:00:00') 
       departureTime=models.TimeField(default='00:00:00') 
       sleeperAvailable=models.BigIntegerField(default=0)
       sleeperWaiting=models.BigIntegerField(default=0)
       acAvailable=models.BigIntegerField(default=0)
       acWaiting=models.BigIntegerField(default=0)
       sleeperPrice=models.BigIntegerField(default=0)
       acPrice=models.BigIntegerField(default=0)
       

class Ticket_details(models.Model):
       ticket_id=models.BigIntegerField()
       pass_name=models.CharField(max_length=100)
       pass_age=models.BigIntegerField()
       gender=models.CharField(max_length=10)
       seat_no=models.BigIntegerField()
       status=models.CharField(max_length=50)
       
