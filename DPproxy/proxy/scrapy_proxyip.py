# -*- coding: utf-8 -*-
# author: itimor

import re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProxyIpFinder():

    def __init__(self, site, tr_rule, ip_rule, port_rule, scheme_rule):
        self.site = site
        self.tr_rule = tr_rule
        self.ip_rule = ip_rule
        self.port_rule = port_rule
        self.scheme_rule = scheme_rule

        # phantomjs
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
        )
        self.driver = webdriver.PhantomJS('../../phantomjs',desired_capabilities=dcap)


    def find(self):
        self.driver.get(self.site)
        table = self.driver.find_elements_by_xpath(self.tr_rule)

        ippool = []
        for ip in table:
            addr = ip.text.split()
            print addr



if __name__ == '__main__':
    proxy = ProxyIpFinder(
        site='http://www.xicidaili.com/nn/',
        tr_rule = '//*[@id="ip_list"]/tbody/tr[position()>1]',
        ip_rule='//*[@id="ip_list"]/tbody/tr[2]/td',
        port_rule='//*[@id="ip_list"]/tbody/tr[2]/td[2]',
        scheme_rule='c',
    )
    proxy.find()
