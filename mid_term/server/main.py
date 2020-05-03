from flask import Flask, request
from google.oauth2 import service_account
from google.cloud import bigquery
cred = service_account.Credentials.from_service_account_file('aibigdata-ntut-107598064-bigquery.json')
client = bigquery.Client(project = 'aibigdata-ntut-107598064', credentials = cred)
app = Flask(__name__)

@app.route('/<string:table>/patch', methods = ['POST'])
def restful(table):
    region = request.form.get('country')
    party = request.form.get('candidate')
    party_votes = request.form.get('votes')
    query = "UPDATE test.president2020 SET party_votes = {} WHERE region like '%{}%' AND party like '%{}%'".format( party_votes, region, party)
    print(query)
    query_job = client.query(query)
    result = query_job.result()
    return query

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
