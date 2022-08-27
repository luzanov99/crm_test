from decimal import DivisionByZero
from tracemalloc import start
from unittest import result
from crm.settings import VIEW_ID
from urllib import request
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import httplib2
from dashboard.models import Metrics
from crm.settings import BASE_DIR

location =BASE_DIR / 'caramel-theory.json'


def get_report(start_date, end_date):
    print(start_date, end_date)
    metrics_names = []
    credentials = ServiceAccountCredentials.from_json_keyfile_name(location, ['https://www.googleapis.com/auth/analytics.readonly'])
    body = {'reportRequests': [{'viewId':VIEW_ID, 
                                'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
                                'metrics': [{'expression': 'ga:users'}, 
                                            {"expression": "ga:sessionsPerUser"},
                                            {"expression": "ga:totalValue"},
                                            {"expression": "ga:transactions"},
                                            {"expression": "ga:transactionsPerUser"},
                                            {"expression": "ga:productRevenuePerPurchase"},
                                            {"expression": "ga:adCost"},
                                            {"expression": "ga:transactionRevenue"},
                                            {"expression": "ga:productAddsToCart"},
                                            {"expression": "ga:revenuePerTransaction"},
                                            ],
                                'dimensions': [{'name': 'ga:yearMonth'}],
                                
                            }]}
    http = credentials.authorize(httplib2.Http())
    service = build('analyticsreporting', 'v4', credentials=credentials)
    response = service.reports().batchGet(body=body).execute()
    metrics_values=response['reports'][0]['data']['rows'][0]['metrics'][0]['values']
    metrics_dics = response['reports'][0]['columnHeader']['metricHeader']['metricHeaderEntries']
    for metric in metrics_dics:
        metrics_names.append(metric['name'][3:])
    result = dict(zip(metrics_names, metrics_values))

    result['users_in_transactions'] =  float(result['transactionsPerUser']) * float(result['transactions'])
    try:
        result['roi'] = (float(result['transactionRevenue']) - float(result['adCost']))/float(result['adCost']) *100
        result['abandoned_carts'] = (float(result['productAddsToCart']) - float(result['transactions']))/float(result['productAddsToCart']) *100
    except ZeroDivisionError:
        result['roi'] = 0 

    #print(result)

    #metric.save()
    return metric
