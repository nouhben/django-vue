from django.db import models

# Create your models here.
class Car(models.Model):
    CAR_TYPE =[
        ('SA','SEDAN'),
        ('SP','SPORT'),
        ('SV','SUV'),
        ('TR','TRUCK'),
    ]
    car_name = models.CharField(max_length=50,default='Ford') 
    car_type = models.CharField(choices=CAR_TYPE, max_length=50) 
    age = models.PositiveSmallIntegerField()
    car_id = models.PositiveIntegerField()

    def __str__(self):
        return f'car number: {self.car_id}'
    