import pymysql
import json

#Configuration Values
endpoint = 'runs.clezslj1op7i.us-west-2.rds.amazonaws.com'
username = 'admin'
password = 'test1234'
database_name = 'Application'

#Connection
connection = pymysql.connect(host=endpoint,user=username,
           password=password,database=database_name)

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
      
    strUserName = event['strUserName']
    strAlias = event['strAlias']
    strImageUrl = event['strImageUrl']
    strBio = event['strBio']
    myCursor = connection.cursor()
    sql = "INSERT INTO tblUsers (strUserName,strAlias,strBio,strImageUrl) VALUES(%S,%S,%S,%S)"
    val = (strUserName,strAlias,strBio,strImageUrl)
    myCursor.execute(sql,val)
    connection.commit()

    return {
        'statusCode': 200,
        'body': json.dumps('User Added, ' + event['strUserName'])
        }
    
    
