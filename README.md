# lax-model

## Workflows

1. Update config.yaml
2. Update schema.yaml (all the columns of data w.r.t. data type)
3. Update params.yaml (giving the model name)
4. Update the entity
5. Update the configuration manager in src config
6. Update the components (data ingestion, data validation, data transformation)
7. Update the pipeline (training & prediction pipeline)
8. Update the main.py
9. Update the app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/nkofficial-1005/lax-model
```
### STEP 01- Create a conda environment after opening the repository

```bash
python -m venv mlproj
```

```bash
mlproj\Scripts\activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=Your-MlFlow-tracking-URL \
MLFLOW_TRACKING_USERNAME=Your-MlFlow-Username \
MLFLOW_TRACKING_PASSWORD=Your-MlFlow-Password \
python script.py

Run this to export as env variables:

```bash

set MLFLOW_TRACKING_URI=Your-MlFlow-tracking-URL

set MLFLOW_TRACKING_USERNAME=Your-MlFlow-Username

set MLFLOW_TRACKING_PASSWORD=Your-MlFlow-Password

```