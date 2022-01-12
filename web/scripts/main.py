#! /usr/bin/env python
'''
2022-01-12 수정사항 : 서버 연동이 원활하게 되지 않을까해서 linux환경에서 돌아가도록 기존 코드를 수정했습니다. 
제가 ubuntu로 돌려봤을 땐 잘 돌아갔는데 ec2 가상환경에선 어떨지 모르겠네요.
헤더를 불러오는 방법도 계속 알아보고 있는데 지난 학기와 마찬가지 이유로 찾을 수가 없네요ㅠㅠ
이 코드는 강의계획안 사이트에서 파일을 자동으로 다운로드하는 코드입니다.
설치해야하는 것 :
beautifulsoup, selenium, pillow, selenium_screenshot
자신의 chrome 버전과 맞는 chrome driver
'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def run():
    print("Test")
