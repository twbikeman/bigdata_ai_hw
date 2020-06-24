from flask import Flask
app = Flask(__name__) 

@app.route('/')
def index():
    return 'hello world!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 443, ssl_context = ('certificate.crt', 'private.key'))
