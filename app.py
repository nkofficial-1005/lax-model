from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from laxProject.pipeline.prediction import PredictionPipeline
# Import Prometheus client functions
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Summary, Gauge, Histogram


app = Flask(__name__) # initializing a flask app

# Example metrics: count total requests and measure request latency
REQUEST_COUNT = Counter('request_count', 'Total number of requests', ['method', 'endpoint'])
REQUEST_LATENCY = Summary('request_latency_seconds', 'Request latency', ['endpoint'])
ERROR_COUNT = Counter("error_count", "Number of errors encountered") #new addition after prom
PREDICTION_HIST = Histogram("prediction_distribution", "Distribution of wine quality predictions", buckets=[3,5,7,10]) #new addition after prom

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
            case_text = request.form['case_text']

            if not case_text.strip():
                return render_template('index.html', error="Please enter a valid case description.")

            #Initialize the PredictionPipeline
            obj = PredictionPipeline()

            #Get prediction using LegalBERT
            predicted_violations = obj.predict(case_text)

            # predict_value = obj.predict(case_text)[0]
            # PREDICTION_HIST.observe(predict_value)

            return render_template('results.html', prediction=predicted_violations)

        except Exception as e:
            print('The Exception message is: ',e)
            ERROR_COUNT.inc() #new addition after prom
            return 'Something is wrong. Please try again.'

    else:
        return render_template('index.html')

# New endpoint for Prometheus to scrape metrics
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)