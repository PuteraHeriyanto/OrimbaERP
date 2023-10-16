from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal,ROUND_HALF_DOWN, ROUND_HALF_UP
import math


class SawnLogInput(models.Model):
    log_id = models.CharField(max_length=100)
    sawn_id =  models.CharField(primary_key=True, max_length=100, unique = True)
    sawn_length = models.IntegerField(default=0)
    sawn_grade = models.CharField(max_length=100, default="")
    diameter_1 = models.IntegerField(default=0)
    diameter_2 = models.IntegerField(default=0)
    average_diameter = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)
        
    class Meta:
        db_table = 'log_cutting"."sawn_log_test' 
        app_label = 'sawnlog_input'
    

    def __str__(self):
	    return self.log_id
    


class SawnLog(models.Model):
    log_id = models.CharField(max_length=100)
    sawn_id =  models.CharField(primary_key=True, max_length=100, unique = True)
    sawn_length = models.DecimalField(max_digits=10, decimal_places=0)
    sawn_grade = models.CharField(max_length=100)
    diameter_1 = models.FloatField()
    diameter_2 = models.FloatField()
    average_diameter = models.DecimalField(max_digits=10, decimal_places=0)
    volume = models.DecimalField(max_digits=10, decimal_places=0)
    

    def save(self, *args, **kwargs):
        self.average_diameter = Decimal(self.diameter_1 + self.diameter_2) / 2
        self.average_diameter = Decimal(math.floor(float(self.average_diameter)))
        self.volume = (self.average_diameter * self.average_diameter * Decimal(0.7854) * self.sawn_length * Decimal(0.000001))
        self.volume = self.volume.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        super(SawnLog, self).save(*args, **kwargs)


    class Meta:
        db_table = 'log_cutting"."sawn_log_test' 
        app_label = 'sawnlog_view'

    
  

class LogList(models.Model):
    log_id = models.CharField(primary_key=True, max_length=100, unique = True)
    stock = models.IntegerField(default=1)

  
    class Meta:
        db_table = 'log_cutting"."log_list_test' 
        app_label = 'loglist_app2' 


# Barcode Project

        
    
        