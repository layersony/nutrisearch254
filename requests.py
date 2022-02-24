from urllib import request
import json

base_url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'


def get_details(query):
  '''
  Get details of food from passed query.
  '''
  req = request.Request(base_url, method='POST')
  req.add_header('Content-Type', 'application/json')
  req.add_header('x-app-id', 'db6249ef')
  req.add_header('x-app-key', '5f05ca24b7db75fd0d05102571367378')
  data= {
    "query": query
  }
  data = json.dumps(data)
  data = data.encode()

  with request.urlopen(req, data=data) as url:
    get_nutrients_data = url.read()
    get_nutrients_response = json.loads(get_nutrients_data)
    details_results = None
    print(details_results)
