import requests
from googletrans import Translator

from django.core import management
from django_cron import CronJobBase, Schedule


def send_sms_group(msgbody='Welcome', lang='hi'):
    x = trans(msgbody, lang)
    z = x.text
    url = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=5eA2hHbuk06KW6ieBIE4kA&senderid=TESTIN&channel=2&DCS=8&flashsms=0&number=917598054350&text=' + "\'" + str(
        z) + "\'" + '&groupid=18114&route=clickhere'
    res = requests.get(url)
    context = {}
    context['res'] = res
    context['url'] = url
    return context


def send_sms(msgbody='Welcome', lang='hi', number='7598054350'):
    x = trans(msgbody, lang)
    print(x.text)
    z = x.text
    url = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=5eA2hHbuk06KW6ieBIE4kA&senderid=TESTIN&channel=2&DCS=8&flashsms=0&number=91' + str(
        number) + '&text=' + "\'" + str(
        z) + "\'" + '&route=clickhere'
    print(url)
    res = requests.get(url)
    context = {}
    context['res'] = res
    context['url'] = url
    return context


def trans(text='hello', lang='ta'):
    translator = Translator()
    word_new = translator.translate(text=text, dest=lang)
    print(word_new)
    return word_new


def bulk_trans(text=['hello', 'good morning'], lang='ta'):
    translator = Translator()
    translations = translator.translate(text, dest=lang)
    words_trans = []
    for i in translations:
        print(i.text)
        words_trans.append(i.text)
    words = {}
    words['trans'] = words_trans
    print(words['trans'])
    return words


class crop_advices_sms(CronJobBase):
    RUN_AT_TIMES = ['6:00', '18:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'accounts.send_advices'

    def do(self):
        pass


"""
# usage
from utilities.send_sms import send_sms
x  = send_sms('<msg body>')
x.json()
"""
