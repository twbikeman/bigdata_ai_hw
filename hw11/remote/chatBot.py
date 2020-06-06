from linebot import LineBotApi
from linebot.models import TestSendMessage 
import chatBotConfig

def webhook(events):
    for event in events:
        __eventDispatcher(event)
    return True

def __eventDispatcher(event):
    lineId = event.source.user_id
    
def pushMessage(message,lineId):
    line_bot_api = LineBotApi(chatBotConfig.accessToken)
    line_bot_api.push_message(lineId,TextSendMessage(text = message))
