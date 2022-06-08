from celery import shared_task
from pool.models import Upload
from bucket import bucket


@shared_task
def upload_image_task(user, image):
    # Upload.objects.create(user=context['user'], image=context['image'])
    Upload.objects.create(user=user[0], image=image[0])
    return True


@shared_task
def delete_object_task(filename):
    bucket.delete_object(filename=filename)
    return True
