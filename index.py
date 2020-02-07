from flask import Flask, request

from flask.logging import default_handler


import logging
app = Flask(__name__)
app.logger.removeHandler(default_handler)
logging.basicConfig(level=logging.DEBUG)
@app.route('/regression', methods=['POST'])
def regression():
    DV = request.get_json()['DV']
    IV = request.get_json()['IV']
    columns = request.get_json()['columns']
    rows = request.get_json()['rows']
    #app.logger.info(str(request.get_json()))
    
    return 'Hello, world!'
