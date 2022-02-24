#! /usr/local/bin/python3
from urllib.error import HTTPError
from flask import Flask, render_template, request, redirect, url_for
from flask_script import Manager, Server
from requests import get_details

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
  try:
    fd_Result = get_details(searchquery)
  except HTTPError:
    fd_Result = None
    pass
  return render_template('results.html', searchquery=searchquery,fd_Result=fd_Result)

# 
manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
  manager.run()