#!/usr/bin/env python
# coding: utf-8
from gevent import monkey
monkey.patch_all()

from celery_tasks import get_page

for x in range(1000):
    get_page.delay("https://ianchenhq.com")
