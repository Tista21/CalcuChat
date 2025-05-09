import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
st.title('Love Bite Chat')
openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  @tool
  def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b
  llm = ChatOpenAI(openai_api_key=openai_api_key)
  llm_with_tools = llm.bind_tools([multiply])
  llm_with_tools.invoke('Hi how are you')
  query = HumanMessage(input_text)
  messages = [query]
  result = llm_with_tools.invoke(messages)
  messages.append(result)
  tool_result = multiply.invoke(result.tool_calls[0])
  messages.append(tool_result)
  messages
  text = llm_with_tools.invoke(messages)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What is the capital of india')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text.content)
