from bigquery_proxy import bigquery_proxy

mybigquery_proxy = bigquery_proxy()
tag1 = {
    'timestamp': '2020-01-22 11:30',
    'bus': '藍333',
    'num': 300
}

tag2 = {
    'timestamp': '2020-01-23 11:30',
    'bus': '藍333',
    'num': 110
}

tag3 = {
    'timestamp': '2020-01-24 11:30',
    'bus': '藍333',
    'num': 220
}

tag4 = {
    'timestamp': '2020-01-25 11:30',
    'bus': '藍333',
    'num': 300
}


mybigquery_proxy.insertRowToBigdata('bus', (tag1, tag2, tag3, tag4))
