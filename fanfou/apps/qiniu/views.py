import uuid

from django.http import JsonResponse
from qiniu import Auth

from .qiniu_settint import access_key, secret_key

# Create your views here.

def get_uptoken(request):
    bucket_name = 'fanfou'
    key = str(uuid.uuid1()).replace('-','')
    q = Auth(access_key=access_key, secret_key=secret_key)
    uptoken = q.upload_token(bucket_name, key, 7200)
    return JsonResponse({'uptoken':uptoken})


def get_downtoken(request):
    domain = request.POST.get('domain')
    key = request.POST.get('key')
    _url = "http://%s/%s"%(domain, key)
    q = Auth(access_key=access_key, secret_key=secret_key)
    url = q.private_download_url(_url, 7200)
    return JsonResponse({'url':url})