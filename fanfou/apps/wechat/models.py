from django.db import models
from common.generic import BM
# Create your models here.
class Wechat(BM):
    appid = models.CharField(max_length=60)
    appsecret = models.CharField(max_length=60)
    token = models.CharField(max_length=60)
    access_token = models.CharField(max_length=60)