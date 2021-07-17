import pymysql
import json
import os 
from dotenv import load_dotenv

load_dotenv()
#Connection
connection = pymysql.connect(host=os.getenv('endpoint'),user=os.getenv('dbusername'),
           password=os.getenv('password'),database=os.getenv('database_name'))

# define the handler function that the Lambda service will use as an entry point
# add context back 
def lambda_handler(event,context):
    
    strUserName = event['strUserName']
    strAlias = event['strAlias']
    strImageUrl = event['strImageUrl']
    strBio = event['strBio']
    myCursor = connection.cursor()
    sql = "INSERT INTO tblUsers (strUserName,strAlias,strBio,strImageUrl) VALUES(%s,%s,%s,%s)"
    val = (strUserName,strAlias,strBio,strImageUrl)
    myCursor.execute(sql,val)
    connection.commit()

    return {
        'statusCode': 200,
        'body': json.dumps(event)
        }


# DUMMY_DATA =  {
# "strUserName" : "localTest1",
# "strAlias" : "localTest1",
# "strImageUrl" : "localTest1",
# "strBio" : "localTest1"

#  }
 
# lambda_handler(DUMMY_DATA)
    
