from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from src.database import db
from src.app import APP

migrate = Migrate(APP, db)
manager = Manager(APP)

manager.add_command('db', MigrateCommand)


# using locally in dev:
#   python3 manage.py db init --directory src/migrations/
#   python3 manage.py db migrate --directory src/migrations/
#   python3 manage.py db upgrade --directory src/migrations/

if __name__ == '__main__':
    manager.run()
