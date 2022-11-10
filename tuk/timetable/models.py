from django.db import models

# Create your models here.
class Timetable(models.Model):
    days_choice=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday')
    ]
    time_choices=[
        ('7-9 am','7-9 am '),
        ('9-11 am','9-11 am '),
        ('11-1 pm','11-1 pm '),
        ('2-4 pm','2-4 pm '),
        ('4-6 pm','4-6 pm '),
    ]
    day =models.CharField(max_length=9, choices=days_choice, null=True,)
    timeslot =models.CharField(max_length=9, choices=time_choices, null=True,)
    unitName = models.CharField(max_length=100)
    venue =  models.CharField(max_length=100)
    lecturer = models.CharField(max_length=100)