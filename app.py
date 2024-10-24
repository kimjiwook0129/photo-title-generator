import streamlit as st
from generate_photo_title import generate_photo_title

st.set_page_config(page_title="사진 제목 생성기", page_icon="📸")

st.markdown("""
    # 📸 사진 제목 생성기 📄
    ### 제목을 짓고 싶은 사진을 올리시면 제목을 지어드립니다.
""", unsafe_allow_html=True)


password = st.text_input("비밀번호", type="password", placeholder="비밀번호를 입력하세요")

instruction = st.text_area(
    "요청사항", "", height=150, 
    placeholder = "원하시는 제목 스타일이나 요청 사항을 적어주세요, 선택 사항입니다.",
    max_chars = 300
)

image = st.file_uploader("사진을 업로드해주세요 (JPG, JPEG, PNG 형식)", type=["jpg", "jpeg", "png"])

if st.button("요청"):
    if not password:
        st.error("비밀번호를 입력해주세요.")
    elif not password == st.secrets['general']["authorization"]:
        st.error("비밀번호가 일치하지 않습니다.")
    elif not image:
        st.error("사진을 업로드해주세요.")
    else:
        try:
            st.markdown(f"""{generate_photo_title(image, instruction)}""")
        except:
            st.error("챗지피티에 문제가 있습니다. 관리자에게 연락해주세요.")


        
