# -*- coding: utf-8 -*-
from linebot import LineBotApi
from linebot.models import TextSendMessage
from flask import Flask, jsonify, request

ACCESS_TOKEN = 'ER+KnU1nE9Z1bDZ4dwNCz7INXVT+9zzFKt4RAzU2e/c2G0c9rB8EhcAFeHEbODRlVume3fQofmza9p+N6pdBP0cXiyNrO71bs89HV1S54X7234j+dGdukvhtBzgdCEv+Cf4VtpkVeIV8r1i0lC9gVQdB04t89/1O/w1cDnyilFU='
app = Flask(__name__)


@app.route('/send_msg', methods=['POST'])
def send_msg():
    # msgの受取
    msg_json = request.get_json()
    msg = msg_json['message']

    if msg is not None:
        send_line_message(msg)

    return jsonify()


def send_line_message(msg):
    line_bot_api = LineBotApi(ACCESS_TOKEN)
    line_bot_api.broadcast(TextSendMessage(text=msg))


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=8080)
