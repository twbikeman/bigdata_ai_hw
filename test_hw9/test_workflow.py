from workflow.engine import GenericWorkflowEngine

def flow1(object, eng):
    print(object + 1)

def flow2(object, eng):
    print(object + 2)

flowEngine = GenericWorkflowEngine()
taskFlow = [flow1, flow2]
flowEngine.callbacks.replace(taskFlow)
flowEngine.process([1])

