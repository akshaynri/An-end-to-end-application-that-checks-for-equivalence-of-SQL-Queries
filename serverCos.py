from bottle import route, run, static_file, response, post, request
from json import dumps
import solver
import os
import logging

@route('/hello')
def hello():
    return "Hello World!"
@route('/')
def server_static():
    return static_file("FrontEnd.html", root='.')
@post('/solve')
def getquerydetails():
     queryparam = request.params.get('query')
     try:
          resultjson = solver.solve(queryparam)
          response.content_type = 'application/json'
          logging.info('JSON result is', resultjson )
     except Exception as e:
          logging.error("Exception occurred", exc_info=True)
     
     return dumps(resultjson)

run(host='0.0.0.0', port=8082, debug=True)
