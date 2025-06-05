import os
import sys

import re
import ssl

from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
Python 연습 문제 15
- 위키피디아 사이트 크롤링하기 (+ https://en.wikipedia.org/wiki/ + 검색어 조합)
- 검색어를 입력 받아 위키피디아 사이트를 크롤링한다
- 위키피디아 내부 페이지에 대한 링크를 크롤링한다 (+ 즉, /wiki/ 로 시작하는 링크)
- 크롤링 한 링크는 파일에 모두 기록한다
"""


# Training 15
def start(args):
	ssl._create_default_https_context = ssl._create_unverified_context
	