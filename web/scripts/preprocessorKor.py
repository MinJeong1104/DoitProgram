# -*- coding: utf-8 -*-

#1. 띄어쓰기
#2. 전처리

from pykospacing import Spacing
from summa.summarizer import summarize

#word_list = [['Description', '본 교과목 은 생애 과정 에서 발생할 수 있는 다양한 건강 과 질병 문제 가 인간 의 삶 에 어떠한 영향 을 미치는지 이해 하고 이와 관련한 사회 복지 제도 와 정책 , 서비스 등 을 포괄적 으로 이해 하는데 목적 이 있다 . 이를 위해 예방 - 치료 - 사회 복귀 의 건강 연속성 차원 에서 의료기관 과 지역 사회 내 다양한 사회 복지 현장 에서 발생 하는 건강 문제 를 통합적 으로 이해 하고 , 의료 사회 복지 실천 과정 과 보건 의료 및 의료 보장 정책 을 학습 함으로써 사회 복지사 로서의 역량 을 향상 한다 . 아울러 변화 하는 의료 환경 에 따른 대응 전략 을 탐색 한다 . 선수 학습 사항 '], ['Prerequisites', '선수 과목 : 사회 복지 개론 , 사회 복지 실천론 ( 또는 사회 복지 실천 기술론 ) 강의 방식 Course '], ['Format', '강의 토론 / 발표 실험 / 실습 현장 실습 기타 Lecture Discussion/Presentation Exper iment/Pr act i cum Field Study Other 50% 40% 10% 0% 0% ( 위 항목 은 실제 강의 방식 에 맞추어 변경 가능 합니다 . ) 강의 진행 방식 설명 ( explanation of course format ) : 본 수업 은 강의 와 토론 , 사례 분석 , 소규모 집단 활동 , 개별 과제 및 팀 프로젝트 수행 등 의 다양한 학 습 방법 을 통해 진행 됩니다 . 본 수업 은 비 대면 수업 방식 으로 Zoom 을 활용 한 실시간 강의 로 진행 됩니다 . | 1 女 大 え 이화 여자 대학교 WHA 교과 목표 Course '], ['Objectives', '1. 보건 의료 와 사회 복지 의 관계 에 대해 이해 한다 . 2. 생애 주기 별 건강 문제 및 건강 관련 이론 에 대해 학습 한다 . 3. 예방 - 치료 - 사회 복귀 의 연속성 을 고려한 다양한 영역 에서 의 보건 및 의료 사회 복지 의 역할 에 대해 이해 한다 . 4. 보건 의료 정책 과 의료 보장 정책 에 대해 파악 한다 . 5. 의료 사회 복지 실천 현장 에 대한 이해 를 바탕 으로 주요 질환 의 심리 사회적 영향 과 지역 및 의료기관 의 사회 복지 서비스 에 대해 학습 한다 . 5. 학습 평가 방식 '], ['Evaluation', '중간 고사 기말 고사 프로젝트 & 발표 개별 과제 참여 도 기타 Midterm Exam Final Exam Projects & Presentation Assignments Par ticipation Other 20% 30% 20% 10% 10% 10% *I IEE 4 l PEER EVALUATION)•] 7 a include '], ['Evaluation', '7 (explanation of evaluation system): 1. 출석 및 수업 참여 ( 10 % ) 2. 중간 고사 ( 20 % ) 3. 기말 고사 ( 30 % ) 4. 개별 과제 ( 10 % ) - 의료 및 건강 관련 도서 ( 또는 관심 이슈 에 대한 학술지 논문 3 편 ) 를 읽고 보고서 작성 ( 구체적인 작성 방법 은 추후 따로 공지 함 ) 5. 팀 프로젝트 & 발표 ( 20 % ) - 의료 사회 복지 실천 개입 대상 과 관련 이슈 에 대한 보고서 작성 및 발표 ( 구체적인 작성 방법 은 추 후 따로 공지 함 ) 6. 퀴즈 / 온라인 토론 참여 ( 10 % ) II. 17 t Course Materials and Additional Readings 1. 77 '], ['Required', '김연수 외 ( 2017 ) . 의료 사회 복지 의 이해 와 실제 . 나눔 의 집 . 4 '], ['Supplementary', '1t '], ['optional', '강흥구 ( 2019 ) . 의료 사회 복지 실천론 . 정민 사 . 조성상 외 ( 2019 ) . 의료 사회 복지 실천론 . 신정 . 주 차별 추가 자료 별도 안내 예정 ( 사이버 캠퍼스 확인 ) 이화 여자 대학교 EWHA IIⅢI . 수업 운영 규정 ']]

#한자 제거하기

def space_kor(word_list):
    new_sent_list = []
    spacing_list = []
    for txt in word_list:
        new_sent_word = []
        print("txt[0]="+str(txt[0]))
        print("txt[1]=" + str(txt[1]))
        new_sent_word.append(str(txt[0]))
        new_sent_word.append(str(txt[1]).replace(" ", ''))
        new_sent_list.append(new_sent_word)

    for txt in new_sent_list:
        new_space_word = []
        spacing = Spacing()
        new_space_word.append(txt[0])
        new_space_word.append(spacing(txt[1]))
        spacing_list.append(new_space_word)

    return spacing_list

def summarzied_kor(spacing_list):
    summarzied_pages=[]
    for page in spacing_list:
        summarzied_word=[]
        if page[0] == 'Description':
            summarzied_word.append(page[0])
            summarzied_word.append(summarize(page[1]))
        else:
            summarzied_word.append(page[0])
            summarzied_word.append(page[1])
        summarzied_pages.append(summarzied_word)

    return summarzied_pages

#이화 대학교 라는 말 모두 제외 / 한자 제외
#prerequisites : 뒤에 강의, 방식, Course 단어 있으면 제외
#Format: 이거 어떻게 정제하냐.. 하여간 보기. / 뒤에 교과목표, Course 단어 있으면 제외
#Evaluation: 이것도 format처럼 정제해야 하는데.... 하.... 아 근데 표로 추출된 거라 걍 제거만 하면 될지도..
#required 그대로 넣기
#Supplementary: