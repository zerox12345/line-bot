from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('1yA3t/Gd7FrTMS5I/Yt06RwQm54OwmE95uOanqhMeKJZDWkFMGSoSUKWyNgGOylt+ExY1+jC52J4V+h3kyEFf7DCjNqBDrqEBUk4umQx3X9O5DtbhmOjxxFn659St6H55EK6BY1QhhGdS91HoXlXlwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('792764ef1c6ad3903e54cf630ee3c0c9')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '哩勒工三小'
    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()