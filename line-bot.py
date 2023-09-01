import json
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


# ===== Line API =====
line_bot_api = LineBotApi('zigiOReM19vRCpOmosB6tYxfcf4SIlYWQMiAoauQ7wU7/4Ma0VVPmmDcV4jZ1mTNFGqLa989uRief1WmllTz1Nxcl5UFnoiHebrHqYPXZpybPfsIa5VLjUKfgUZaaPjhiYCTRpCIgGNTGtwhNGrDAwdB04t89/1O/w1cDnyilFU=') #Chanel acces token
handler = WebhookHandler('b793b34d0434b0bac546f7babb42e1e0') # Chenal Secert
group = 'C8a140ef6439bac7968277b24ef3bf528' #Group ID
# =====================


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        data = json.dumps(request.json)
        print(data)
        
        text_message = TextSendMessage(text=data)
        print(text_message)
        line_bot_api.push_message(group, text_message) # push message buy via Line

        # print(request.data)
        return 'success', 200
    else:
        abort(400)

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    print(body)
    return 'OK'

if __name__ == '__main__':
    app.run()

