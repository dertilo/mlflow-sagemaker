import os

import mlflow.sagemaker as mfs


if __name__ == '__main__':
    experiment_id = "0"
    run_id = "8edb7181fbec4651af03147fe2086db4"  # see in file: mlruns/.../artifacts/model/MLmodel
    region = "eu-central-1"
    aws_id = os.popen("aws sts get-caller-identity --query Account --output text").read().strip("\n")
    arn = "arn:aws:iam::{aws_id}:role/your-role".format(aws_id=aws_id)
    app_name = "diabetes-class"
    model_uri = "mlruns/%s/%s/artifacts/model" % (experiment_id, run_id)
    image_url = aws_id + ".dkr.ecr." + region + ".amazonaws.com/mlflow-pyfunc:1.8.0"  # change to your mlflow version

    mfs.deploy(app_name=app_name,
               model_uri=model_uri,
               region_name=region,
               mode="create",
               execution_role_arn=arn,
               image_url=image_url,
               instance_count=1,
               instance_type="t3.micro"
               )