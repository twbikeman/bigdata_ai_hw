from flask import Flask, request
app = Flask(__name__)


@app.route('/<string:name>', methods = ['GET','POST'])
def home(name):
    request.form['test']
    return "success!"
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 80, debug = True)
