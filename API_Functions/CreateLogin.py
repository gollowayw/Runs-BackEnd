import boto3
import boto3.dynamodb.table
import os 
from dotenv import load_dotenv

load_dotenv()

def createLogin(dynamodb,body):
     print(body)

     table:  boto3.dynamodb
     table = dynamodb.Table(os.getenv('UserTable'))
     table.put_item(Item=body)



     return {
        'statusCode': 200,
        'body': "I hope it worked holy shit"
        }
    
