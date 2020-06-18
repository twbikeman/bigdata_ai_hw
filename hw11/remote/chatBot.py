from linebot import LineBotApi
from linebot.models import TextSendMessage 
import chatBotConfig

def webhook(events):
    for event in events:
        __eventDispatcher(event)
    return True

def __eventDispatcher(event):
    lineId = event.source.user_id
    if event.type == "message":
        pushMessage('good', lineId)
    
def pushMessage(message,lineId):
    line_bot_api = LineBotApi(chatBotConfig.accessToken)
    line_bot_api.push_message('twbikeman',TextSendMessage(text = message))
