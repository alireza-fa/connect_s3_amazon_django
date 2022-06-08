for use:
  - docker network create s3_main
  - docker network create s3_nginx_network
  - docker volume create s3_static_volume
  - docker-compose up -d
  - docker exec -it s3_app bash
  - python manage.py collectstatic
  - done
