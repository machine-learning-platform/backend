from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
from flask.logging import default_handler


import logging
app = Flask(__name__)
app.logger.removeHandler(default_handler)
logging.basicConfig(level=logging.DEBUG)
@app.route('/regression', methods=['POST'])
def regression():
    # DV = request.get_json()['DV']
    # IV = request.get_json()['IV']
    X = np.array(request.get_json()['X'][:-1])
    y = np.array(request.get_json()['y'][:-1])
    reg = LinearRegression().fit(X,y)
    app.logger.info(reg.score(X, y))
    app.logger.info(reg.coef_) 
    app.logger.info(reg.intercept_)   
    return jsonify({
        'score': reg.score(X, y),
        'coefficients': list(reg.coef_),
        'intercept': reg.intercept_
    })
