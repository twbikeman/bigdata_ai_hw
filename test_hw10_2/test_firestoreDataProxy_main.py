import firestoreDataProxy
from firestoreDataProxy import DataProxy

dataproxy = DataProxy()
data = {'name': 'Brayn', 'salary': 100}
print(data)
dataproxy.setBot(data)
print(data)
