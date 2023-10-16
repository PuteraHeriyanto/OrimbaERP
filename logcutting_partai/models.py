from django.db import models
from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal,ROUND_HALF_DOWN, ROUND_HALF_UP
import math



# class Partai(models.Model):
#     partai_id = models.CharField(primary_key=True,max_length=100)

#     def __str__(self):
# 	    return self.partai_id

#     class Meta:
#         db_table = 'log_cutting"."partai' 



class Partai(models.Model):
    partai_id = models.CharField(primary_key=True, max_length=100, unique = True)
    supplier_id = models.CharField(max_length=100)
    date_arrived = models.DateField()
    # supplier_id = models.CharField(max_length=100)
    log_cost = models.DecimalField(max_digits=10, decimal_places=2)
    # species_id = models.CharField(max_length=100)
    # log_colour = models.CharField(max_length=100)
    # log_length = models.DecimalField(max_digits=10, decimal_places=0)
    # diameter_1 = models.FloatField()
    # diameter_2 = models.FloatField()
    # average_diameter = models.DecimalField(max_digits=10, decimal_places=0)
    # volume_bruto = models.DecimalField(max_digits=10, decimal_places=2)
    # volume_trimming = models.DecimalField(max_digits=10, decimal_places=2)
    # volume_netto = models.DecimalField(max_digits=10, decimal_places=2)
    # is_deleted = models.BooleanField(default=False)


    # def save(self, *args, **kwargs):
    #     self.average_diameter = Decimal(self.diameter_1 + self.diameter_2) / 2
    #     self.average_diameter = Decimal(math.floor(float(self.average_diameter)))
    #     self.volume_bruto = (self.average_diameter * self.average_diameter * Decimal(0.7854) * self.log_length * Decimal(0.0001))
    #     self.volume_bruto = self.volume_bruto.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    #     self.volume_netto = Decimal(self.volume_bruto - self.volume_trimming)
    #     self.volume_netto = self.volume_netto.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    #     super(LogList, self).save(*args, **kwargs)


    def __str__(self):
        return f"partai_id: {self.partai_id}, supplier_id: {self.supplier_id}"
        
    class Meta:
        db_table = 'log_cutting"."partai' 
        app_label = 'partai_app' 




class Supplier(models.Model):
    supplier_id = models.CharField(primary_key=True,max_length=100)
    supplier_name = models.CharField(max_length=100)

    # def __str__(self):
	#     return self.supplier_id
       
    class Meta:
        db_table = 'log_cutting"."supplier_logs'
        app_label = 'supplier_app2'




# class Species(models.Model):
#     species_id = models.CharField(primary_key=True,max_length=100)
#     species_name = models.CharField(max_length=100)

#     def __str__(self):
# 	    return self.species_id
      
#     class Meta:
#         db_table = 'log_cutting"."species_log' 




# class LogList(models.Model):
#     log_id = models.CharField(primary_key=True, max_length=100, unique = True)
#     partai_id = models.CharField(max_length=100)
#     tanggal_kedatangan = models.DateField()
#     supplier_id = models.CharField(max_length=100)
#     grade = models.CharField(max_length=100)
#     species_id = models.CharField(max_length=100)
#     log_colour = models.CharField(max_length=100)
#     log_length = models.IntegerField()
#     diameter_1 = models.IntegerField()
#     diameter_2 = models.IntegerField()
#     average_diameter = models.IntegerField()
#     volume_bruto = models.IntegerField()
#     volume_trimming = models.IntegerField()
#     volume_netto = models.IntegerField()
#     # created_at = models.DateTimeField()
    

#     def __str__(self):
# 	    return self.name
    
#     class Meta:
#         # db_table = 'LogCutting_schema"."log_list_test' 
#         db_table = 'log_cutting"."log_list_test' 




# class Transaction(models.Model):
#     bill_for = models.CharField(max_length=100)
#     issue_date = models.DateField()
#     due_date = models.DateField()
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     status = models.CharField(max_length=10)

#     created_time = models.DateTimeField(auto_now_add=True)
#     updated_time = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = 'transaction'
#         verbose_name_plural = 'transactions'

#     @property
#     def status_info(self):
#         res = {'class': None}

#         if self.status == "Paid":
#             res['class'] = 'text-success'
#         elif self.status == "Due":
#             res['class'] = 'text-warning'
#         elif self.status == "Canceled":
#             res['class'] = 'text-danger'

#         return res
