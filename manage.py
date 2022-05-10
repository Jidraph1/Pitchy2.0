from app import create_app,db
from flask_script import Manager, Server
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Shell
from app.models import Users, Pitch, Comment

#creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Users = Users, Pitch=Pitch,Comment=Comment )

if __name__ == '__main__':
    manager.run(host="0.0.0.0",port=5019)