pip install langchain-openai
pip install streamlit
import streamlit as st
from langchain_openai import ChatOpenAI
st.title('Love Bite Chat')
openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = ChatOpenAI(temperature=0.8, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are three indication that i am in love?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
