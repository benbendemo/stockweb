from flask_script import Manager
from flask_migrate import MigrateCommand
from App import create_app
import os

env = os.environ.get('FLASK_ENV', 'develop')
app = create_app(env)
print('manage.py app:', dir(app), app)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

@manager.option('-h', '--host', dest='host', default='127.0.0.1')
@manager.option('-p', '--port', dest='port', type=int, default=5000)
@manager.option('-w', '--workers', dest='workers', type=int, default=4)
@manager.option('-r', '--reload', dest='_reload', default=False)
@manager.option('-D', '--daemon', dest='daemon', default=False)
@manager.option('-k', '--worker-class', dest='worker_class', default='gevent')
def gunicorn(host, port, workers, daemon, _reload, worker_class):
    """Start the Server with Gunicorn"""
    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {
                'bind': '{0}:{1}'.format(host, port),
                'workers': workers,
                'daemon': daemon,
                'reload': _reload,
                'worker_class': worker_class
            }

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()

if __name__ == '__main__':
    manager.run()
