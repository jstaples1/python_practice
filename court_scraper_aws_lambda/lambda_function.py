import sys
sys.path.append('/home/jason/CODE/python/git_repos/python_practice/court_scraper_aws_lambda/anything')
#sys.path.append('./lib')
sys.path.append('/var/task/court_scraper_aws_lambda/anything')


import json

from bs4 import BeautifulSoup
from courtscraper_funcs import functions

def lambda_handler(event, context):
    if event == None or event.get('queryStringParameters') == None:
        return {
            'statusCode': 200,
            'body': json.dumps(functions.getResponseBody(None,None))
        } 
    elif event.get('queryStringParameters').get('date') == None:
        return {
            'statusCode': 200,
            'body': json.dumps(functions.getResponseBody(None,None))
        } 


    return {
        'statusCode': 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "accept, accept-encoding, authorization, content-type, dnt, origin, user-agent, x-csrftoken, x-requested-with, hx-request,hx-current-url, hx-trigger",
            "Content-Type": "text/html",
            "Cache-Control": "no-cache"
        },
        'body': functions.getResponseBody(event['queryStringParameters']['date'],event['queryStringParameters']['courtNumber'])
    }


#######Code to Test lambda function locally#######
event = {}
query_params = {'date': '2023-12-21','courtNumber': '2'}
#event['queryStringParameters'] = {'other_date': '2023-12-21'}
event['queryStringParameters'] = query_params
#print(lambda_handler(event, None))    
print(lambda_handler(None, None))    
