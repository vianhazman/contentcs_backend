#content.cs-service
This repository is the backend service for content.cs.ui.ac.id.

##How to run

Initialize database information in `.env` with structure as below.
```
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=contentcs_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
This service uses `docker-compose` to build and run.

run the service in background using
```docker-compose up -d```

build the image using ```docker-compose build```

##How to inspect runtime

see the nginx logs
```docker-compose logs nginx```

see the django-app logs
```docker-compose logs app```

see the postgres logs
```docker-compose logs db```