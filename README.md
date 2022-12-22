# FastAPI   CLOUD BOX
This API service is supposed upload and download files for users 

# How to run a project
--Rename `docker-compose copy.yml` to `docker-compose.yml`
--Run `sudo docker-compose up --build` to create container


--Open `http://localhost:8008/ `in browser to open project 


--Open `http://localhost:8008/docs`in browser to open API docs page


--Connect to DB `sudo docker-compose exec db psql --username=admin --dbname=facloud`

--Run `sudo docker exec -it cloud python manage.py test` for test

