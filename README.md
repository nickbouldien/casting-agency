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
TODO 
```

### Start dev server
(using port 8080 here)
```bash
export FLASK_APP=src/app.py
export FLASK_ENV=development
flask run -h localhost -p 8080
```

### API Endpoints
GET 
/actors
/movies

DELETE
/actors/
/movies/

POST
/actors
/movies

PATCH
/actors/
/movies/
