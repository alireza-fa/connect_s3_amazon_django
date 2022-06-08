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

درباره پروژه:

  در این پروژه من جنگو را به s3 آمازون متصل کرده ام برای ذخیره سازی فایل های medida در باکت های آروان کلود.
  
  در این پروژه بجز استفاده از باکت های آروان کلود برای media فایل ها، پروژه را به celery نیز متصل کرده ام. زیرا در دیلیت کردن و ... ممکن است تاخیری بوجود بیاید که با سلری این را برای کاربران غیر قابل لمس کردن میکنیم.
  
  همچنین پروژه داکرایز شده است تا به سادگی بتوانید با چند خط کد اجرایش کنید.
    
 نکته:
 
   در پروژه های واقعی ما تنظیماتی مانند SECRET_KEY و یا تنظیمات s3 را در یک فایل دیگری برای مثال local_settings.py قرار میدهیم و در settings.py پروژه import میکنیم تا در گیت هاب این تنظیماتی که امنیتی هستند قابل مشاهده نباشد.

  امیدوارم این پروژه برای شما مفید باشد.
