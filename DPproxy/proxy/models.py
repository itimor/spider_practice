# -*- coding: utf-8 -*-
# author: itimor

from django.db import models

class ProxyPool(models.Model):
    ip = models.CharField(unique=True, max_length=21, verbose_name=u'代理ip')
    scheme = models.CharField(max_length=11, verbose_name=u'协议')
    port = models.IntegerField(u'端口')
    alive = models.BooleanField(default=True)

    def __unicode__(self):
        return '{}//:{}:{}'.format(self.scheme,self.ip,self.port)

    class Meta:
        verbose_name = u'代理ip池'
        verbose_name_plural = u'代理ip池'


class ProxySite(models.Model):
    siteName = models.CharField(unique=True, max_length=21, verbose_name=u'免费代理网站')
    xpath_ip_rule = models.CharField(max_length=50, verbose_name=u'xpath匹配ip规则')
    xpath_scheme_rule = models.CharField(max_length=50, verbose_name=u'xpath匹配协议规则')
    xpath_port_rule = models.CharField(max_length=50, verbose_name=u'xpath匹配端口规则')

    def __unicode__(self):
        return '{}'.format(self.siteName)

    class Meta:
        verbose_name = u'免费代理网站'
        verbose_name_plural = u'免费代理网站'
