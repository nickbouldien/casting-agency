import os

test = "casting_agency_test"
dev = "casting_agency_dev"
# TODO - get prod db path from heroku
prod = ""

environment = os.environ.get('FLASK_ENV', 'production')
print("*** environment *** => ", environment)

if environment == "test":
    database_name = test
elif environment == "development":
    database_name = dev
else:
    database_name = prod

SQLALCHEMY_DATABASE_URI = f'postgresql://nick@localhost:5432/{database_name}'
print("SQLALCHEMY_DATABASE_URI: ", SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_TRACK_MODIFICATIONS = False
