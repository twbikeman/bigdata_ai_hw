from flask import Flask, request, Response
from linebot import WebhookParser, LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import InvalidSignatureError
import chatBotConfig
import chatBot

app = Flask(__name__)

@app.route("/chatBotService", methods = ['POST'])
def chatBotService():
    line_bot_api = LineBotApi(chatBotConfig.channel[accessToken])
    line_bot_api.push_message('U6d0dd5cef5b317dcaf921b599f06ef27',TextSendMessage(text = 'message'))
    return Response(status = 200)

    # signature = request.headers('X-Line-Signature')
    # body = request.get_data(as_text = True)
    # channelSecret = chatBotConfig.channel['channelSecret']
    # try:
    #     events = WebhookParser(channelSecret).parse(body, signature)
    # except InvalidSignatureError:
    #     print("Invalid signature. Please check your channel access token/channel secret.")
    #     state = False
    # print("test")
    # state = chatBot.webhook(events)
    # if state:
    #     return Response(status = 200)
    # else:
    #     return Response(status = 500)


@app.route('/')
def hello():
    return 'hello world'

if __name__=='__main__':
    app.run(host = '0.0.0.0', debug = True) 

