# FastAPI   CLOUD BOX
This API service is supposed upload and download files for users 


# Technology Stack:

    FastAPI
    Uvicorn (server)
    Pytest
    Sqlalchemy
    Postgres

# How to run a project

--Run `sudo docker-compose up --build` to create container


--Open `http://localhost:8008/ `in browser to open project 


--Open `http://localhost:8008/docs` in browser to open API docs page


--Connect to DB `sudo docker-compose exec db psql --username=admin --dbname=facloud`

--Run `sudo docker exec -it facloud_web_1 alembic init migrations` to make migrations



