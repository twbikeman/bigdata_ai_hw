import time
from monitor import monitor

@monitor
def test(dataModel):
    time.sleep(5)

if __name__ == '__main__':
    dataModel = {
        'timestamp': 123
    }
    test(dataModel)
    
    
