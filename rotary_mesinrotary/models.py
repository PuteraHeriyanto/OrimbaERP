from django.db import models

from django.contrib.auth.models import User
from decimal import Decimal,ROUND_HALF_DOWN, ROUND_HALF_UP
import math



class MesinRotary(models.Model):
    # log_id = models.CharField(primary_key=True, max_length=100, unique = True)
    # sawn_id =  models.CharField(max_length=100)
    id_mesin_rotary = models.CharField(primary_key=True, max_length=100, unique = True)
    # sawn_id =  models.CharField(primary_key=True, max_length=100, unique = True)
    mesin_rotary = models.FloatField(max_length=100)
    # sawn_grade = models.CharField(max_length=100)
    # diameter_1 = models.CharField(max_length=100)
    # diameter_2 = models.CharField(max_length=100)
    # average_diameter = models.CharField(max_length=100)
    # volume = models.CharField(max_length=100)

    # def __str__(self):
    #     return f"supplier_id: {self.supplier_id}"
        
    class Meta:
        # unique_together = (('log_id', 'sawn_id'),)
        db_table = 'rotary"."id_mesin_rotary' 
        app_label = 'mesinrotary_app'
    


# class LogList(models.Model):
#     log_id = models.CharField(primary_key=True, max_length=100, unique = True)
#     stock = models.IntegerField(default=1)

    # def __str__(self):
    #     return f"log_id: {self.log_id}, sawn_id: {self.sawn_id}"
        
    # class Meta:
    #     db_table = 'log_cutting"."log_list_test' 
    #     app_label = 'loglist_app2' 

    
    
        