from BigqueryProxy import BigqueryProxy

if __name__ == '__main__':
    test = BigqueryProxy()
    monitorTag =  {
        'id': 'id',
        'taskName': 'taskName',
        'beginTime': 123,
        'endTime': 123,
        'taskTime': 123              
    }

    test.insertRowToBigdata('mytest', (monitorTag,))
    
    
    
