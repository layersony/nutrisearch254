from flask import Flask
from flask_script import Manager, Server

# Server
manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
  manager.run()