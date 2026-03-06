'''
import streamlit as st
import numpy as np
with st.chat_message("user"):
 st.write("Hello 👋")
with st.chat_message("assistant"):
  st.write("Yes, would you like? 👋")
with st.chat_message("Johnny"):
 st.write("Yes, would you like? 👋")
 st.bar_chart(np.random.randn(30, 3))
'''
import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
 with st.chat_message("assistant"):
    st.write(f"User has sent the following prompt: {prompt}")

