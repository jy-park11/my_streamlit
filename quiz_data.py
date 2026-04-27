import streamlit as st
import time

@st.cache_data
def get_questions():
    time.sleep(2) 
    return [
        # 객관식
        {"type" : "multiple", "q": "피카츄의 타입은?", "options": ["번개", "노말", "전기"], "a": "전기"},
        {"type" : "multiple", "q": "꼬부기의 최종 진화체의 이름은?", "options": ["팽도리", "거북왕", "어니부기"], "a": "거북왕"},
        {"type" : "multiple", "q": "잠만보의 타입은?", "options": ["격투", "노말", "땅"], "a": "노말"},
        {"type" : "multiple", "q": "포켓몬스터 애니메이션 속 주인공 지우가 놓아준 포켓몬은?", "options": ["피카츄", "찌르버드", "피죤투"], "a": "피죤투"},
        {"type" : "multiple", "q": "진화형이 존재하지 않는 포켓몬은?", "options": ["피츄", "라프라스", "토게피"], "a": "라프라스"},

        # 주관식
        {"type": "text", "q": "포켓몬스터의 마스코트 캐릭터 이름은 무엇인가요?", "a": "피카츄"},
        {"type": "text", "q": "지우의 고향 마을 이름은?", "a": "태초마을"}
    ]