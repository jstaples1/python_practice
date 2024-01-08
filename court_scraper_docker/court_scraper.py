import sys
#sys.path.append('/home/jason/CODE/python/git_repos/python_practice/court_scraper_docker/lib')
sys.path.append('/home/jason/CODE/python/git_repos/python_practice/court_scraper_docker/courtscraper/app/')



sys.path.append('/app/lib')


import json

from bs4 import BeautifulSoup
import functions


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
query_params = {'date': '2024-01-05','courtNumber': '2'}
event['queryStringParameters'] = query_params
#lambda_handler(event, None)    
#print(functions.getResponseBodies(event['queryStringParameters']['date']))
functions.getResponseBodies(event['queryStringParameters']['date'])    


