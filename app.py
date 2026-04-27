import streamlit as st
import login      # auth.py 불러오기
import quiz_data   # quiz_data.py 불러오기
import time

def main():
    # 세션 초기화
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False

    # 화면 분기
    if not st.session_state.is_logged_in:
        st.sidebar.title("과제 제출 정보")
        st.sidebar.info("학번: 2023204075\n\n이름: 박준영")

        login.login_logic() # auth.py의 함수 실행
    else:
        # [조건 4] 퀴즈 기능
        st.title("포켓몬 주관식/객관식 퀴즈")
        questions = quiz_data.get_questions()
        user_answers = []

        with st.form("quiz_form"):
            for i, item in enumerate(questions):
                st.markdown(f"**Q{i+1}. {item['q']}**")

                # [핵심] 타입에 따라 위젯 분기
                if item["type"] == "multiple":
                    # 객관식
                    ans = st.radio(f"선택하세요 ({i})", item["options"], key=f"q{i}", label_visibility="collapsed")
                    user_answers.append(ans)

                else:
                    # 주관식 (st.text_input 사용)
                    ans = st.text_input("답안을 입력하세요", key=f"q{i}", placeholder="정답 입력")
                    user_answers.append(ans.strip()) # 앞뒤 공백 제거
            
            if st.form_submit_button("결과 확인"):
                with st.spinner('채점 중 입니다...'):
                    time.sleep(2)
                score = 0
                for idx, user_ans in enumerate(user_answers):
                    if user_ans == questions[idx]["a"]:
                        score += 1
                
                if score == len(questions):
                    st.image("pikachu.png", caption="축하합니다! 당신은 포켓몬 마스터!", width=300)
                    st.success(f"최종 점수: {score} / {len(questions)}")
                elif score >= 5:
                    st.success(f"최종 점수: {score} / {len(questions)}")
                elif 5 > score >= 3:
                    st.warning(f"최종 점수: {score} / {len(questions)}")
                else:
                    st.error(f"최종 점수: {score} / {len(questions)}")

        if st.sidebar.button("로그아웃"):
            st.session_state.is_logged_in = False
            st.rerun()

if __name__ == "__main__":
    main()