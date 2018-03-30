import requests


def send_sms_group(msgbody='Welcome'):
    url = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=5eA2hHbuk06KW6ieBIE4kA&senderid=TESTIN&channel=2&DCS=8&flashsms=0&number=917598054350&text=' + str(
        msgbody) + '&groupid=18114&route=clickhere'
    res = requests.get(url)
    return res


def send_sms(msgbody='Welcome'):
    url = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=5eA2hHbuk06KW6ieBIE4kA&senderid=TESTIN&channel=2&DCS=8&flashsms=0&number=917598054350&text=' + str(
        msgbody) + '&route=clickhere'
    res = requests.get(url)
    return res


"""
# usage
from utilities.send_sms import send_sms
x  = send_sms('<msg body>')
x.json()
"""
