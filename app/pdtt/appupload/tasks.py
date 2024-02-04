from .models import File
from celery import shared_task


@shared_task
def reprocessed(serializer_data_id):
    f = File.objects.get(id=serializer_data_id)
    f.processed = True
    f.save()
