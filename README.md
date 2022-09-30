# djangoProject UrbanData v1.0.0 Backend 

Backend project for **Urbandata test** platform

### Prerequisites

docker 


## Run the Application

```
git clone https://github.com/scruzdata/urban-src.git
cd urban_src
 - create .env and edit variables(same variables as file ".env.example") 
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
# Otras Consideraciones, dudas y decisiones:
No habia usado aún postgreSQL con Gis y me costo un poco la instalación y montarlo todo con docker (fué donde más tiempo perdí)

En cuanto a la estructura de los datos lo guardé en campos simples tipo IntegerField, porque no sabía que significaba 
cada uno, algún campo lo guarde como tipo  "choise" ejemplo "property_type" (teniendo la leyenda de cada valor, en el admin 
es mas entendible pero no quise perder mucho el tiempo en eso y lo hice sólo para esa variable)

# Cuestiones adicionales
- ¿Como sería de fácil realizar una búsqueda por ID sobre esos activos? 
  
En ese caso cree la API 
  "http://localhost:8080/data/retails/?id_uda=54-94183090" filtrando por el id es facil obtener cualquier propiedad y
  añadiendo un identificador único de tipo primary_key=True, hace mas rapida la llamada.
    
- ¿Y una búsqueda por distancia a unas coordenadas establecidas?
  
http://localhost:8080/data/property-by-distance-and-coordinates/?distance=700&latitude=40&longitude=-3
  Para este caso opté por usar la funcion 
  "GeometryDistance" de django gis, creando una variable adicional "distance" para cada propiedad que guarda la 
  distancia entre 2 coordenadas (coordenada de la propiedad y la coordenada que uso en la API). 
  
- ¿Para 1 millón de activos la solución que has pensado sería igual de eficiente?
  
Para espacios de alta dimension (1 millón de activos por ejemplo) la funcion "GeometryDistance" usa  el 
  algoritmo (KNN) y por tanto no es tán eficiente, su eficiencia disminuye a medida que crece la dimensionalidad, 
  es decir la distancia euclidiana es inútil en dimensiones altas porque todos los vectores son casi equidistantes 
  al vector de consulta de la búsqueda.
  

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

