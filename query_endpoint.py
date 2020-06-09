import boto3
import numpy as np
import pandas as pd
from sklearn import datasets

# Load Diabetes datasets
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

# Create a pandas DataFrame that will serve as a sample input for the deployed ElasticNet model
Y = np.array([y]).transpose()
d = np.concatenate((X, Y), axis=1)
cols = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6', 'progression']
data = pd.DataFrame(d, columns=cols)
query_df = data.drop(["progression"], axis=1).iloc[[0]]

# Convert the sample input dataframe into a JSON-serialized pandas dataframe using the `split` orientation
input_json = query_df.to_json(orient="split")

import json
app_name = "diabetes-class"
region = "eu-central-1"


def query_endpoint(app_name, input_json):
    client = boto3.session.Session().client("sagemaker-runtime", region)

    response = client.invoke_endpoint(
        EndpointName=app_name,
        Body=input_json,
        ContentType='application/json; format=pandas-split',
    )
    preds = response['Body'].read().decode("ascii")
    preds = json.loads(preds)
    print("Received response: {}".format(preds))
    return preds


print(
    "Sending batch prediction request with input dataframe json: {}".format(input_json))

# Evaluate the input by posting it to the deployed model
prediction1 = query_endpoint(app_name=app_name, input_json=input_json)


