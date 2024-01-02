from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "wellcome all"

##working with link: http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=4&entropy=1
@app.route('/predict')
def predict_note_auth():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "Predict value is: " +  str(prediction)

##using postman to test file TestFileAPI.csv
@app.route('/predictfile', methods = ["POST"])
def predict_note_auth_file():
    df_test= pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "Predict value is: " +  str(list(prediction))


if __name__=='__main__':
    app.run()