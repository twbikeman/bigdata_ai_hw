from flask import Flask, request
from google.oauth2 import service_account
from google.cloud import bigquery

cred = service_account.Credentials.from_service_account_file('aibigdata-ntut-107598064-bigquery.json')
client = bigquery.Client(project = 'aibigdata-ntut-107598064', credentials = cred)

app = Flask(__name__)




@app.route('/<string:table>/post', methods = ['POST'])
def restful(table):
    region = request.form.get('region')
    key = request.form.get('key')
    value = request.form.get('value')
    query = "INSERT test.{} (region, key, value) VALUES('{}', '{}', {})".format(table, region, key, value)
    query_job = client.query(query)
    result = query_job.result()

    return query

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

    
    

