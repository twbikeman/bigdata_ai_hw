from workflow.engine import GenericWorkflowEngine
from functools import wraps


my_engine = GenericWorkflowEngine()


def print_data(obj, eng):
    print(obj.data)


def my(obj,eng):
    obj.data = obj.data * 10;
    print(obj.data)

def add_data(number_to_add):
    @wraps(add_data)
    def _add_data(obj, eng):
        obj.data += number_to_add
    return _add_data

my_workflow_definition = [add_data(1), print_data,my]

class MyObject(object):
    def __init__(self, data):
        self.data = data

my_object0 = MyObject(0)
my_object1 = MyObject(1)

my_engine.callbacks.replace(my_workflow_definition)
my_engine.process([my_object0, my_object1])
my_engine.process([my_object0, my_object1])
