# djangoProject UrbanData v1.0.0 Backend 

Backend project for **Urbandata test** platform

### Prerequisites

docker 


## Run the Application

```
git clone https://github.com/scruzdata/urban-src.git
cd urban_src
 - add .env 
 - run the command: docker-compose up --build -d --remove-orphans
 - run the migrate command: docker-compose exec api python3 manage.py migrate --noinput
 - create superuser: docker-compose exec api python3 manage.py createsuperuser	

Check django admin in the browser: http://localhost:8080/admin/

- then run the command: docker-compose exec api python3 manage.py shell

to load assets data to backend, run these commands:
>>> from properties import load
>>> load.run()
>>> quit()



### API Requests ###
Open Postman and make the following get requests
1. Return all properties
GET http://localhost:8080/data/retails/

2. Return a property based on id_uda
GET http://localhost:8080/data/retails/?id_uda=54-94183090

3. Get properties based on distance and a point of coordinates:
- params: 
    > distance: distance in km (int)
    > latitude: latitude coordinate (float)
    > longitude: longitude coordinate (float)
    
GET http://localhost:8080/data/property-by-distance-and-coordinates/?distance=700&latitude=40&longitude=-3

4. down volumen
docker-compose down

```

# Built With

* [Python](https://www.python.org/) - One of the best programming language
* [Django](https://www.djangoproject.com/) - The best high-level Python Web framework
* [DRF](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs
* [Postgresql](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database


## Versioning

1.0.0 

* API to save data in backend
* API to retrieve all properties from backend
* API to retrieve all properties from backend based on distance and a coordinate point 



## Authors

* **Sergio Cruz Bardera** - [Linkedin](https://www.linkedin.com/in/sergiocruzb/)

## License

No License

