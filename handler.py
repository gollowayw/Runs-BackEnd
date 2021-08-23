from API_Functions.CreateLogin import createLogin
from API_Functions.RetrieveAllUsers import retrieveAllUsers
import boto3
import os 

#Connection

dynamodb = boto3.resource('dynamodb',region_name='us-west-2')

# define the handler function that the Lambda service will use as an entry point
# add context back 
def lambda_handler(event,context):
    

    path = event["path"]
    

    if path == "/CreateLogin":
       body = event["body"]
       return createLogin(dynamodb,body)
    if path == "/RetrieveAllUsers":
        return retrieveAllUsers(dynamodb)
    
    return {
        'statusCode': 503,
        'body': {"message":"failed to find method"}
        }

