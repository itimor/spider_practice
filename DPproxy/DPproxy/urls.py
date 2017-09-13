# -*- coding: utf-8 -*-
# author: itimor

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from proxy.views import ProxyViewSet

router = DefaultRouter()
router.register(r'proxypool', ProxyViewSet)

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api/', include(router.urls)),

                  # 用户认证
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
              ]
