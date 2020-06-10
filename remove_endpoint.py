import mlflow.sagemaker as mfs
app_name = "diabetes-class"
region = "eu-central-1"

mfs.delete(app_name=app_name, region_name=region, archive=False)