from flask_script import Manager
from flask_migrate import MigrateCommand
from App import create_app
import os

env = os.environ.get('FLASK_ENV', 'testing')
app = create_app(env)
print('manage.py app:', dir(app), app)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
