from .models import File
from celery import shared_task


@shared_task
def reprocessed():
    f = File.objects.get(id=1)
    f.processed = True
    f.save()
