import streamlit as st
st.write("이것은 기본 텍스트 출력입니다.")


import openai

user_api_key = st.text_input("키를 입력해주세요.")

from openai import OpenAI

client = OpenAI(api_key = user_api_key)
prompt = st.text_input("프롬프트를 입력해주세요.")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
st.markdown("### 💡 GPT의 답변:")
st.write(completion.choices[0].message.content)