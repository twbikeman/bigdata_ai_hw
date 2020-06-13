import time
import threading

from BigqueryProxy import BigqueryProxy

bigquery = BigqueryProxy()

def monitor(function):
    def _monitor(*args, **kwargs):
        dataModel = args[0]
        id = str(dataModel['timestamp'])
        t0 = time.time()
        result = function(*args)
        t1 = time.time()
        taskName = function.__name__
        monitorTag = {
            'id': id,
            'taskName': taskName,
            'beginTime': t0,
            'endTime': t1,
            'taskTime': round((t1-t0) * 1000, 2)
        }
        t = threading.Thread(target = bigquery.injectMonitorTag, args = (monitorTag,))
        print(monitorTag)
        t.start()
    return _monitor


