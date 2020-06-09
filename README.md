# mlflow-sagemaker
* [](https://docs.databricks.com/applications/mlflow/quick-start-python.html)

```
pip install awscli --upgrade --user
aws configure
```
* profiles/users: `cat ~/.aws/credentials` and `cat ~/.aws/config`
1. create named role: `aws configure --profile <user_name>`
2 tell aws cli which user to use: `export AWS_PROFILE=<user_name>`
3. build&push docker image to Elastic Container Registry (ECR): `mlflow sagemaker build-and-push-container`
    * this serves as a base image for all models deployed by mlflow, so fully independent of the actual model and its requirements
    * see: https://eu-central-1.console.aws.amazon.com/ecr/repositories?region=eu-central-1