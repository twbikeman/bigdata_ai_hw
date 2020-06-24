from flask import Flask, request, Response

from linebot import WebhookHandler, LineBotApi
from linebot.models import MessageEvent, TextMessage, TextSendMessage


import chatBotConfig


app = Flask(__name__) 

line_bot_api = LineBotApi(chatBotConfig.channel['accessToken'])
handler = WebhookHandler(chatBotConfig.channel['channelSecret'])




@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = event.message.text))
    


@app.route('/callback', methods=['POST'])
def callback():
    print("test")
    signature = request.headers['X-Line-Signature']  
    body = request.get_data(as_text = True)
    app.logger.info("Request body: " + body)


    handler.handle(body, signature)
    return 'OK'


@app.route('/')
def hello():
    return 'Ok'





if __name__ == '__main__':
    app.run(host = '0.0.0.0')
