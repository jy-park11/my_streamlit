import streamlit as st

def login_logic():
    st.title("🔐 로그인")
    with st.form("login"):
        user_id = st.text_input("아이디")
        user_pw = st.text_input("비밀번호", type="password")
        if st.form_submit_button("접속"):
            if user_pw == "1234" and user_id == 'admin':
                st.session_state.is_logged_in = True
                st.session_state.user_id = user_id
                st.rerun()
            else:
                st.error("아이디 또는 비밀번호를 다시 입력해주세요.")