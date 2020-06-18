# Casting Agency
Capstone project

## Development Setup
using Python 3.7.x (actual version needed for deployment to heroku can be found in [./runtime.txt](runtime.txt))

### Virtual Environment
```bash
$ virtualenv venv
$ source venv/bin/activate
```

### Install Dependencies
After creating the virtual environment
```bash
$ pip3 install -r requirements.txt
```

### Dev Database Setup
create the database
```bash
$ createdb casting_agency_dev
```

run migrations
```bash
$ flask db init --directory src/migrations/
$ flask db migrate --directory src/migrations/
$ flask db upgrade --directory src/migrations/
```

### Start dev server
(using port 8080 here)
```bash
export FLASK_APP=src/app.py
export FLASK_ENV=development
flask run -h localhost -p 8080
```

### Running tests
```bash
$ dropdb casting_agency_test
$ createdb casting_agency_test

$ psql casting_agency_test < src/database/casting_agency_test_db.psql
$ source setup_tests.sh
$ python3 -m unittest -v test_app.py
```


## API Endpoints
### Overview
  * GET
    * /actors
    * /movies
    * /actors/{int:actor_id}
    * /movies/{int:movie_id}
    * /actors/{int:actor_id}/details
    * /movies/{int:movie_id}/details
  * POST
    * /actors
    * /movies
  * PATCH
    * /actors/{int:actor_id}
    * /movies/{int:movie_id}
  * DELETE
    * /actors/{int:actor_id}
    * /movies/{int:movie_id}

### Detailed Information / Examples

#### generic endpoints
##### GET /ping
* General:
  * an endpoint strictly used as a health check (make sure the app is up and running)
* Example: `curl https://casting-agency-1.herokuapp.com/ping`

#### movie endpoints
##### GET /api/movies
* General:
  * Get a list of all movies
* Example: `curl https://casting-agency-1.herokuapp.com/api/movies`

##### GET /api/movies/{int:movie_id}/details
* General:
  * Get detailed information about a movie
  * RBAC: Assistant, Director, Producer 
* Example:
```bash
curl --request GET \
  --url https://casting-agency-1.herokuapp.com/api/movies/1/details \
  --header "authorization: Bearer ${BEARER_TOKEN}"
```

##### POST /api/movies
* General:
  * create a new movie
  * RBAC: Producer 
* Example:
```bash
curl --request POST \
  --url https://casting-agency-1.herokuapp.com/api/movies \
  --data '{
      "title": "star wars",
      "releaseDate": "1970-07-28T21:45:23Z",
      "website": "http://www.starwars.com",
      "imageLink": "http://www.somestarwarsimage.com"
    }'
  --header "authorization: Bearer ${BEARER_TOKEN}"
```

##### PATCH /api/movies/{int:movie_id}
* General:
  * update new movie
  * RBAC: Director, Producer 
* Example:
```bash
curl --request POST \
  --url https://casting-agency-1.herokuapp.com/api/movies \
  --data '{
      "title": "star wars",
      "releaseDate": "1970-07-28T21:45:23Z",
      "website": "http://www.starwars.com",
      "imageLink": "http://www.somestarwarsimage.com"
    }'
  --header "authorization: Bearer ${BEARER_TOKEN}"
```



## Authentication and RBAC information
### roles
There are three roles:
- assistant
- director
- producer

the assistant can:
get the movies and actors

the director can:
get/create/update/delete the actors, get/update the movies

the producer can:
get/create/update/delete the actors, get/create/update/delete the movies


### hosting directions
the app is hosted on heroku

##### Create the app
heroku create casting-agency-1

##### Add git remote for Heroku to the local repository (if needed)
git remote add heroku https://git.heroku.com/casting-agency-1.git

##### Add postgresql add on for the database
heroku addons:create heroku-postgresql:hobby-dev --app casting-agency-1

##### check the app config
heroku config --app casting-agency-1

##### add env vars on heroku
heroku dashboard -> settings -> config vars

##### push to heroku
git push heroku master

##### run db migrations
heroku run python manage.py db upgrade --app casting-agency-1 --directory src/migrations/
