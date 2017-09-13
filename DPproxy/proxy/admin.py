# -*- coding: utf-8 -*-
# author: itimor

from django.contrib import admin
from models import ProxyPool

class ProxyAdmin(admin.ModelAdmin):
    list_display = ('ip', 'scheme', 'port', 'speed', 'alive')


admin.site.register(ProxyPool, ProxyAdmin)
