from flask import Flask, request, Response
from linebot import WebhookParser
from linebot.exceptions import InvalidSignatureError
import chatBotConfig
import chatBot

app = Flask(__name__)

@app.route("/chatBotService", method = ['POST'])
def chatBotService():
    signature = request.headers('X-Line-Signature')
    body = request.get_data(as_text = True)
    channelSecret = chatBotConfig.channel['channelSecret']
    try:
        events = WebhookParser(channelSecret).parse(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        state = False
    state = chatBot.webhook(events)
    if state:
        return Response(status = 200)
    else:
        return Response(status = 500)


@app.route('/')
def hello():
    return 'hello world'

if __name__=='__main__':
    app.run(host = '0.0.0.0', debug = True) 

