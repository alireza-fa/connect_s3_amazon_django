from celery import shared_task
from pool.models import Upload
from bucket import bucket


@shared_task
def delete_object_task(filename):
    bucket.delete_object(filename=filename)
    return True
