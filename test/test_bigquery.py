from google.oauth2 import service_account
from google.cloud import bigquery

cred = service_account.Credentials.from_service_account_file('aibigdata-ntut-107598064-bigquery.json')
client = bigquery.Client(project = 'aibigdata-ntut-107598064', credentials = cred)
# table =  client.dataset('test').table('my');
# schema = [bigquery.SchemaField('region', 'STRING'), bigquery.SchemaField('key', 'STRING'), bigquery.SchemaField('value', 'INTEGER')]
# insertData = [{'region': '美國', 'key': '1', 'value': 100}]
# result = client.insert_rows(table, insertData, selected_fields = schema)
# print(result)
# query_job = client.query(
# """
# UPDATE test.my SET value = 288 WHERE region LIKE '%美國%'
# """
# )
query_job = client.query(
# """
# INSERT test.my (region, key, value) VALUES ('美國','1',200)
# """
"""
UPDATE test.my SET value = 288 WHERE region LIKE '%屏東縣%'
"""
)

results = query_job.result()
