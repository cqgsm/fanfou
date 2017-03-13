from requests import get
from hashlib import sha1
from requests import get, post
from json import loads, JSONDecodeError
from django.conf import settings
from django.core.cache import cache

class WeChatBase():
    # get access token
    # ?grant_type=client_credential&appid=APPID&secret=APPSECRET
    GET_ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token'
    GRANT_TYPE_CLIENT_CREDENTIAL = 'client_credential'
    GET_WECHAT_SERVERIP_LIST_URL = 'https://api.weixin.qq.com/cgi-bin/getcallbackip'

    def __init__(self, appid=None, appsecret=None, token=None):
        self.appid = appid or settings.WECHAT['APPID']
        self.appsecret = appsecret or settings.WECHAT['APPSECRET']
        self.token = token or settings.WECHAT['TOKEN']

    @property
    def access_token(self):
        access_token = cache.get(self.appid)
        if access_token:
            return access_token
        else:
            params = {"grant_type":self.GRANT_TYPE_CLIENT_CREDENTIAL, "appid":self.appid, "secret":self.appsecret}
            access_token_dict = self.request_wechat(url=self.GET_ACCESS_TOKEN_URL, params=params)
            access_token = access_token_dict.get('access_token')
            cache.set(self.appid, access_token, 7000)
            return access_token

    def get_wechat_serverip_list(self):
        wechat_serverip_dict = self.request_wechat(url=self.GET_WECHAT_SERVERIP_LIST_URL,
                                                   params={'access_token':self.access_token})
        return wechat_serverip_dict.get('ip_list')

    def request_wechat(self, url, method='GET', params=None):
        if method=='GET':
            response = get(url=url, params=params)
            if response.status_code == 200:
                try:
                    json_dict = loads(response.text)
                except JSONDecodeError:
                    raise AssertionError('invalid appid,secret')
                else:
                    if json_dict.get('errcode', None):
                        raise AssertionError('invalid appid,secret,errcode:%s,errmsg:%s'%(json_dict.get('errcode'),
                                             json_dict.get('errmsg')))
                    else:
                        return json_dict
            else:
                raise AssertionError('wechat server connection failure')


