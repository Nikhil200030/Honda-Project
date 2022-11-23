#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 21:06:35 2018

@author: vivekkalyanarangan
"""

import pickle
from flask import Flask, request, redirect, url_for
from flasgger import Swagger
import numpy as np
import pandas as pd


#with open('./rf.pkl', 'rb') as model_file:
#   model = pickle.load(model_file)
filename = 'rf.pkl'
#model = pickle.load(open(filename, 'rb'))
app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def predict_irisp():
  return redirect(url_for("predict_iris"))

@app.route('/predict')
def predict_iris():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")
    
    prediction = 1 # model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    return str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_iris_file():
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = 1 # model.predict(input_data)
    return "aaaaa" #str(list(prediction))

if __name__ == '__main__':
    app.run(port=5010,debug=True)



    
    
    

    
    
    
    
    
    
    
    
    
    
    