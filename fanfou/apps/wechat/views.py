#coding=utf-8
from json import dumps

from django.http import HttpResponse
from django.conf import settings

from fanfou.apps.wechat.wechat import WeChatBase
from fanfou.apps.wechat.utils import check_signature
# Create your views here.

def wechat_main(request):
    if request.method == "GET":
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        token = settings.WECHAT.get('TOKEN')
        if check_signature(signature, timestamp, nonce, echostr, token):
            return HttpResponse(echostr)
        else:
            return HttpResponse('no wechat')

def get_access_token(request):
    wechat = WeChatBase()
    serverip_list = dumps(wechat.get_wechat_serverip_list())
    return HttpResponse(wechat.access_token + serverip_list)