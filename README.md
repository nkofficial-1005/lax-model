# lax-model

## Workflows

1. Update config.yaml
2. Update schema.yaml (all the columns of data w.r.t. data type)
3. Update params.yaml (giving the model name)
4. Update the entity
5. Update the configuration manager in src config
6. Update the components (data ingestion, data validation, data transformation)
7. Update the pipeline (whole MLOps & prediction pipeline)
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


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 418295710894.dkr.ecr.us-east-2.amazonaws.com/lax-model

	
## 4. Create EC2 machine (Amazon Linux/Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine :
### The following commands are for the Amazon Linux Machine
	
	#optinal

	sudo yum update -y

	sudo yum upgrade -y #updates your package index and installs available updates.
	
	#required to install docker

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo yum install -y docker #installs Docker from the default repositories.

    sudo service docker #start starts the Docker service (optional)

	sudo usermod -aG docker ec2-user #adds the default user (usually ec2-user) to the Docker group so you can run Docker commands without sudo Adjust the username if needed.

	newgrp docker #applies the new group membership immediately. Alternatively, you can log out and back in.

    docker --version #check the version of the docker service running.
	
## 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one.
    
    Here we are connecting github with the AWS EC2 instance. So, whenever updating the code to github, the AWS EC2 instance code would be updated along with the deployment.


## 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-2 (for Ohio)

    AWS_ECR_LOGIN_URI = demo>>  418295710894.dkr.ecr.us-east-2.amazonaws.com

    ECR_REPOSITORY_NAME = lax-model



## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

