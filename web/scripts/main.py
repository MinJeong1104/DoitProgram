#크롤링 호환을 위한 초기버전 test
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from AClass.models import Class
def run():
    url = "https://eureka.ewha.ac.kr/eureka/my/public.do?pgId=P531005519"
    op=Options()
    op.add_experimental_option('prefs',{'download.default_directory':r'C:\Users\mocar\Desktop\down'})
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument('--disable-dev-shm-usage')
    op.add_argument('blink-settings=imagesEnabled=false')
    op.add_argument('--disable-gpu')
    op.add_argument("--remote-debugging-port=9222")
    op.add_experimental_option("excludeSwitches", ["enable-automation"])
    op.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=op,executable_path='/usr/local/bin/chromedriver')
    browser.get(url)
    browser.implicitly_wait(2)

    # 미리 조건 설정 (일단 대충했어요 테스트용!! 입력이나 체크 안할거면 그냥 엔터치심 되어요)
    print("맞으면 1")
    qEng = input("영어강의인가요? : ")
    qRem = input("원격강의인가요? : ")
    print("\n 단답형")
    classNum = input("학수번호? : ")
    classN = input("강의명? : ")
    # 영어강의 체크박스 체크.
    if qEng == "1":
        englishCheck = browser.find_element_by_id(
            "mainframe_VFrameSet_WorkFrame_Child__form_div_Work_div_search_ckbEngChk_chkimg")
        englishCheck.click()
    else:
        print()
    # 원격강의 체크박스 체크.
    if qRem == "1":
        remoteCheck = browser.find_element_by_id(
            "mainframe_VFrameSet_WorkFrame_Child__form_div_Work_div_search_ckbOnChk_chkimg")
        remoteCheck.click()
    else:
        print()
    # 학수번호 text box
    className = browser.find_element_by_id(
        'mainframe_VFrameSet_WorkFrame_Child__form_div_Work_div_search_ipbSubjectCd_input')
    className.click()  # 클릭을 하지 않고 send keys를 사용하면 오류가 납니다...  ㅠㅠ 한참 헤맸네요 click 필수!!
    className.send_keys(classNum)
    time.sleep(3)  # sleep을 쓰지 않으면 selenium이 개복치처럼 종료되기 때문에 시간을 줍니다
    # 그래서 좀 시간이 걸릴 수 있어요! 기다리면 결과가 나올거에요
    # 만약 갑자기 꺼지는 오류가 계속 난다면 sleep의 값을 좀 더 늘려주면 됩니다!
    # 교과목명 text box
    className = browser.find_element_by_id(
        'mainframe_VFrameSet_WorkFrame_Child__form_div_Work_div_search_ipbSubjectNm_input')
    className.click()
    className.send_keys(classN)
    time.sleep(3)
    btn = browser.find_element_by_xpath(
        "//*[@id='mainframe_VFrameSet_WorkFrame_Child__form_div_Work_div_search_btnSearchTextBoxElement']/div")
    btn.click()
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    # print(soup.text)    #줄줄줄 출력됨
    # print(soup.prettify())  #html이 이쁘게 출력됨
    number = soup.find('div', id="mainframe_VFrameSet_WorkFrame_Child__form_div_Work_grxMain_body_gridrow_0_cell_0_1GridCellTextContainerElement").text
    subnum = soup.find('div', id="mainframe_VFrameSet_WorkFrame_Child__form_div_Work_grxMain_body_gridrow_0_cell_0_2GridCellTextContainerElement").text
    title = soup.find('div', id="mainframe_VFrameSet_WorkFrame_Child__form_div_Work_grxMain_body_gridrow_0_cell_0_3GridCellTextContainerElement").text
    div_course= soup.find('div', id="mainframe_VFrameSet_WorkFrame_Child__form_div_Work_grxMain_body_gridrow_0_cell_0_4GridCellTextContainerElement").text
    professor=soup.find('div',id="mainframe_VFrameSet_WorkFrame_Child__form_div_Work_grxMain_body_gridrow_0_cell_0_8GridCellTextContainerElement").text
    
    crawled_time=datetime.now()
    Class(number=number, subnum=subnum, title=title, div_course=div_course, professor=professor, crawled_time=crawled_time).save()
    print(number, subnum, title, div_course, professor)
