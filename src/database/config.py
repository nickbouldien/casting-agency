import os

test = "casting_agency_test"
dev = "casting_agency_dev"


environment = os.environ.get('ENVIRONMENT', 'dev')
print("*** environment *** => ", environment)

if environment == "test":
    database_name = test
else:
    database_name = dev

SQLALCHEMY_DATABASE_URI = f'postgresql://nick@localhost:5432/{database_name}'
print("SQLALCHEMY_DATABASE_URI: ", SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_TRACK_MODIFICATIONS = False
