#!/usr/bin/env python
# coding: utf-8
import json
import logging
import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def download_link(directory, url):
    logger.info('Downloading %s', url)
    download_path = directory / os.path.basename(url)
    res = requests.get(url, stream=True)
    with open(download_path, 'wb') as f:
       for chunk in res.iter_content(chunk_size=1024):
           if chunk: # filter out keep-alive new chunks
               f.write(chunk)

def setup_download_dir():
    download_dir = Path('data')
    if not download_dir.exists():
       download_dir.mkdir()
    return download_dir
