from django.db import models
from django.utils.translation import ugettext_lazy as _

from fanfou.apps.common.generic import BM
# Create your models here.

class Dating(BM):
    PAY_METHOD_CHOICES = (
        (0,'女方付款'),
        (1,'男方付款'),
        (2,'AA'),
    )
    DATING_STATUS_CHOICES = (
        (0, 'start'),
        (1, 'meet'),
        (2, 'end'),
        (3, 'cancel'),
    )
    title = models.CharField(_('title'), max_length=30)
    description = models.CharField(_('description'), max_length=120, blank=True, null=True)
    location = models.CharField(_('location'), max_length=20)
    dating_time = models.DateTimeField(_('dating time'))
    pay_method = models.IntegerField(_('pay method'), choices=PAY_METHOD_CHOICES)
    pictures = models.TextField(_('pictures'), blank=True, null=True)
    status = models.IntegerField(_('status'), choices=DATING_STATUS_CHOICES, default=0)

    class Meta:
        verbose_name = _('dating')
        verbose_name_plural = _('dating')
        db_table = 'dating'

    def __str__(self):
        return self.title


class Participant(BM):
    dating = models.ForeignKey(Dating)
    agree = models.NullBooleanField(blank=True, null=True)

