from fastapi import FastAPI
import pandas as pd 
import json, csv, joblib
from models import Iris, request_body

app = FastAPI()

MEDIA_ROOT = "iris.csv"

@app.get("/")
async def root():
    return "Bienvenido FastAPI"

@app.get("/iris")
async def iris():
    df = pd.read_csv(MEDIA_ROOT)
    data = df.to_json(orient="index")
    data = json.loads(data)
    return data

@app.post("/insertdata")
async def insertdata(item: Iris):
    with open(MEDIA_ROOT, 'a', newline='') as f:
        fieldnames = ['sepal_length','sepal_width',
                      'petal_length','petal_width',
                      'species']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'sepal_length': item.sepal_length,
                        'sepal_width': item.sepal_width,
                        'petal_length': item.petal_length,
                        'petal_width': item.petal_width,
                        'species': item.species})
    return item

@app.put("/updatedata/{item_id}")
async def updatedata(item_id: int, item: Iris):
    df = pd.read_csv(MEDIA_ROOT)
    df.loc[df.index[-1], 'sepal_length'] = item.sepal_length
    df.loc[df.index[-1], 'sepal_width'] = item.sepal_width
    df.loc[df.index[-1], 'petal_length'] = item.petal_length
    df.loc[df.index[-1], 'petal_width'] = item.petal_width
    df.loc[df.index[-1], 'species'] = item.species
    df.to_csv(MEDIA_ROOT, index=False)
    return {"item_id": item_id, **item.dict()}
    
@app.delete("/deletedata")
async def deletedata():
    df = pd.read_csv(MEDIA_ROOT)
    df.drop(df.index[-1], inplace=True)
    df.to_csv(MEDIA_ROOT, index=False)
    return "Eliminado"

@app.post('/predict')
async def predict(data: request_body):
    test_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    clf = joblib.load('model.pkl')
    prediction = clf.predict(test_data)[0]
    if int(prediction)==0:
        prediction = 'Iris-Setosa'
    elif int(prediction)==1:
        prediction = 'Iris-Virginica'
    elif int(prediction)==2:
        prediction = 'Iris-Versicolour'
    
    return {'class': prediction}