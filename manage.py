from flask import Flask, render_template, request, redirect, url_for
from flask_script import Manager, Server
app = Flask(__name__)

# view function
@app.route('/')
def index():
  return render_template('index.html')

# Server
manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
  manager.run()