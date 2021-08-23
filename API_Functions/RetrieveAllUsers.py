import boto3
import os 
from dotenv import load_dotenv

load_dotenv()

def retrieveAllUsers(dynamodb):
    
    table = dynamodb.Table(os.getenv('UserTable'))
    value = table.scan()

    return {
            "statusCode":200,
            "body":value["Items"]}