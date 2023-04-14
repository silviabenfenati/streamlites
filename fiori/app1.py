import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('**Iris database analysis**')

df_fiori = pd.read_csv("iris.csv")

st.dataframe(df_fiori)

#background
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://upload.wikimedia.org/wikipedia/commons/d/db/Iris_versicolor_4.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         
         unsafe_allow_html=True
     )
add_bg_from_url() 

audio_file = open("rick.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")