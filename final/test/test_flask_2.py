from flask import Flask, request, Response

from linebot import WebhookParser, LineBotApi
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


import chatBotConfig

from fetch import fetch


app = Flask(__name__) 

line_bot_api = LineBotApi(chatBotConfig.channel['accessToken'])

query = fetch()

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']  
    body = request.get_data(as_text = True)
    events = WebhookParser(chatBotConfig.channel['channelSecret']).parse(body, signature)
    lineId = events[0].source.user_id
    bus = events[0].message.text
    query.set(bus)
    pic_url = 'https://storage.googleapis.com/aibigdata-ntut-107598064.appspot.com/bus/1593174590.jpg'
    if (query.gettime()):
        text = query.getbus() + '\n' + query.getdest() + '\n' + query.gettime()
    else:
        text = query.getbus() + '\n' + query.getdest() + '\n' + query.getstatus()

    print(text)
    line_bot_api.push_message(lineId, TextSendMessage(text = text, disable_web_page_preview = True))
    line_bot_api.push_message(lineId, ImageSendMessage(original_content_url='https://storage.googleapis.com/aibigdata-ntut-107598064.appspot.com/bus/1593174590.jpg', preview_image_url = 'https://storage.googleapis.com/aibigdata-ntut-107598064.appspot.com/bus/1593174590.jpg'))
    return 'OK'


@app.route('/')
def hello():
    return 'Ok'





if __name__ == '__main__':
    app.run(host = '0.0.0.0')
