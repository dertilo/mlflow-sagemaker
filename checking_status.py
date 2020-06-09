

if __name__ == '__main__':
    import boto3
    app_name = "diabetes-class"
    region = "eu-central-1"


    def check_status(app_name):
        sage_client = boto3.client('sagemaker', region_name=region)
        endpoint_description = sage_client.describe_endpoint(EndpointName=app_name)
        endpoint_status = endpoint_description["EndpointStatus"]
        return endpoint_status


    print("Application status is: {}".format(check_status(app_name)))