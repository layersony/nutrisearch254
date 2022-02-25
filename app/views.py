from urllib.error import HTTPError
from flask import Flask, render_template, request, redirect, url_for
from app.requests import get_details
from app import app

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
