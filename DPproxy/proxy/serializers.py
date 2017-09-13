# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from models import ProxyPool


class ProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProxyPool
        fields = ('url', 'id', 'ip', 'scheme', 'port', 'speed', 'alive')
