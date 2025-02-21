from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from laxProject.pipeline.prediction import PredictionPipeline
# Import Prometheus client functions
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Summary


app = Flask(__name__) # initializing a flask app

# Example metrics: count total requests and measure request latency
REQUEST_COUNT = Counter('request_count', 'Total number of requests', ['method', 'endpoint'])
REQUEST_LATENCY = Summary('request_latency_seconds', 'Request latency', ['endpoint'])

@app.before_request
def before_request():
    # You can add logic here to start a timer if desired
    pass

@app.after_request
def after_request(response):
    # Increment the request count for the given endpoint and method
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    return response

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')

# New endpoint for Prometheus to scrape metrics
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)