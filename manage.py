from flask import Flask, render_template, request, redirect, url_for
from flask_script import Manager, Server
app = Flask(__name__)

# view function
@app.route('/')
def index():
  searchquery = request.args.get('searchquery')
  if searchquery:
    return redirect(url_for('foodResults', searchquery=searchquery))
  return render_template('index.html')


@app.route('/results/<searchquery>', methods=['GET', 'POST'])
def foodResults(searchquery):
  print(searchquery)
  return render_template('results.html', fd_Result=fd_Result)

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
  manager.run()