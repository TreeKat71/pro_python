#!/usr/bin/env python
# coding: utf-8
from celery import Celery
import requests

app = Celery('tasks', broker='redis://')

@app.task
def add(x,y):
    return x + y

@app.task
def get_page(url):
    res = requests.get(url)
    return res.text
