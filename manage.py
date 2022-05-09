from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()