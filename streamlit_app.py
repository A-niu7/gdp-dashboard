import streamlit as st
import pandas as pd
import numpy as np

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")