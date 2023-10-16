from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SawnLog
from .views import SawnLogCreateView 


@receiver(post_save, sender=SawnLogCreateView.model)
def delete_numeric_sawn_ids(sender, instance, **kwargs):
    # Delete records with `sawn_id` containing only numeric characters
    SawnLog.objects.filter(sawn_id__regex=r'^\d+$').delete()