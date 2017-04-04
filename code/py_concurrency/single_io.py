import logging
import os
from time import time

from download import setup_download_dir, download_link

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

def main():
    ts = time()
    download_dir = setup_download_dir()
    links = ['http://img3.6comic.com:99/2/103/861/001_mdh.jpg',
            'http://img3.6comic.com:99/2/103/861/002_9uj.jpg',
            'http://img3.6comic.com:99/2/103/861/003_c8x.jpg',
            'http://img3.6comic.com:99/2/103/861/004_y3b.jpg',
            'http://img3.6comic.com:99/2/103/861/005_hu6.jpg']
    for link in links:
        download_link(download_dir, link)
    print('Took {}s'.format(time() - ts))

if __name__ == '__main__':
    main()
