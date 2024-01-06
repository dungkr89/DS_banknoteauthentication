from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)  ##Using http://127.0.0.1:5000/apidocs/
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)



@app.route('/')
def welcome():
    return "wellcome all"

##working with link: http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=4&entropy=1
@app.route('/predict')
def predict_note_auth():
    #For swagger
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "Predict value is: " +  str(prediction)

##using postman to test file TestFileAPI.csv
@app.route('/predictfile', methods = ["POST"])
def predict_note_auth_file():
    #For swagger
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - file: variance
        in: formData
        type: file
        required: true
    responses:
        200:
            description: The output values
        
    """
    df_test= pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "Predict value is: " +  str(list(prediction))


if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)