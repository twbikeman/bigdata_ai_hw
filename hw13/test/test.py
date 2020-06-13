import random
from workflow.engine import GenericWorkflowEngine
import time
from monitor import monitor

@monitor
def recognize(dataModel, eng):
    runtime = random.random() * 0.100 + 0.800
    time.sleep(runtime)
    print(runtime)

@monitor
def capture(dataModel, eng):
    runtime = random.random() * 0.100 + 0.01
    time.sleep(runtime)
    print(runtime)

@monitor
def notify(dataModel, eng):
    runtime = random.random() * 0.100 + 1.700
    time.sleep(runtime)
    print(runtime)

    
if __name__ == '__main__':
    taskflow = [recognize, capture, notify]
    flowEngine = GenericWorkflowEngine()
    flowEngine.callbacks.replace(taskflow)

    dataModel = {
        'timestamp': int(time.time())
    }
    flowEngine.process([dataModel])
    
    
    
    
    
