# connect s3 amazon in django

for use:

  - set s3 configs * settings.py *
  - docker network create s3_main
  - docker network create s3_nginx_network
  - docker volume create s3_static_volume
  - docker-compose up -d
  - docker exec -it s3_app bash
  - python manage.py collectstatic
  - done
  
Technologies used:
  - django
  - rabbitmq
  - celery
  - boto3

About the project:

  - This project connects our media files to Amazon S3.
  - It is also connected to the celery and can be used when needed.
