# Casting Agency
Capstone project

## Development Setup
using Python 3.7

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
    * /movies/{int:movie_id}k

### Detailed Information / Examples



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
