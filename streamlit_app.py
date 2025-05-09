# import streamlit as st
# st.write("이것은 기본 텍스트 출력입니다.")


# import openai

# user_api_key = st.text_input("키를 입력해주세요.")

# if user_api_key:

#     from openai import OpenAI

#     client = OpenAI(api_key = user_api_key)
#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.markdown("### 💡 GPT의 답변:")
#     st.write(completion.choices[0].message.content)

import streamlit as st
import openai

# 기본 제목과 설명 추가
st.title("💬 ChatGPT와 대화하기")
st.write("OpenAI GPT 모델과 대화할 수 있는 간단한 앱입니다. 🔥")

# API 키 입력
#방법1 user_api_key = st.text_input("🔑 OpenAI API 키를 입력해주세요", type="password")
#방법2 user_api_key ="이곳에 키를 직접 입력하면 키 입력필요없음- 그러나 위험!!"
#방법3
user_api_key = st.secrets["openai"]["api_key"      

# 프롬프트 입력 및 결과 출력
if user_api_key:
    openai.api_key = user_api_key
    prompt = st.text_area("✏️ GPT에게 보낼 메시지를 입력하세요")

    if prompt:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 GPT의 답변:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"⚠️ 오류가 발생했습니다: {e}")
else:
    st.info("🔑 먼저 API 키를 입력해주세요.")

