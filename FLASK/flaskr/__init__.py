import numpy as np
from flask import Flask, request, render_template
import pandas as pd
import json, csv, joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return 'Bienvenido a Flask' 

@app.route('/iris', methods=['GET'])
def irisdata():
    df = pd.read_csv('iris.csv')
    describe = df.describe().to_json(orient='index')
    describe = json.loads(describe)
    return describe

@app.route('/insertData', methods=['POST'])
def insertdata():
    data = request.data
    data = json.loads(data)
    
    with open('iris.csv', 'a', newline='') as f:
        
        fieldnames = ['sepal_length', 'sepal_width',
                     'petal_length', 'petal_width',
                     'species']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'sepal_length': data['sepal_length'],
                      'sepal_width': data['sepal_width'],
                      'petal_length': data['petal_length'],
                      'petal_width': data['petal_width'],
                      'species': data['species']})
        print("Writing complete")
    return data

@app.route('/updateData', methods=['PUT'])
def updatedata():
    data = request.data
    data = json.loads(data)
    df = pd.read_csv('iris.csv')
    
    df.loc[df.index[-1], 'sepal_length'] = data['sepal_length']
    df.loc[df.index[-1], 'sepal_width'] = data['sepal_width']
    df.loc[df.index[-1], 'petal_length'] = data['petal_length']
    df.loc[df.index[-1], 'petal_width'] = data['petal_width']
    df.loc[df.index[-1], 'species'] = data['species']
    
    df.to_csv('iris.csv', index=False)
    result = df.iloc[-1].to_json(orient='index')
    return json.loads(result)

@app.route('/deleteData', methods=['DELETE'])
def deletedata():
    df = pd.read_csv('iris.csv')
    df.drop(df.index[-1], inplace=True)
    df.to_csv('iris.csv', index=False)
    result = df.iloc[-1].to_json(orient='index')
    return result

@app.route("/result", methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        clf = joblib.load('model.pkl')
        sepal_length = request.form.get("sepal_length")
        sepal_width = request.form.get("sepal_width")
        petal_length = request.form.get("petal_length")
        petal_width = request.form.get("petal_width")
        
        X = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
        prediction = clf.predict(X)[0]
        
        if int(prediction)==0:
            prediction = 'Iris-Setosa'
        elif int(prediction)==1:
            prediction = 'Iris-Virginica'
        elif int(prediction)==2:
            prediction = 'Iris-Versicolour'
        else:
            prediction = ""

    return render_template('index.html', output = prediction)

if __name__ == '__main__':
    app.run(debug=True)