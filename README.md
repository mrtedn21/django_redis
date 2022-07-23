To run this project make these command:

```shell
git clone https://github.com/mrtedn21/django_redis.git
cd django_redis
docker-compose up --build
docker exec -it django_redis-api-1 bash
python3 manage.py migrate
python3 manage.py create_users
```

and go to localhost:8000
