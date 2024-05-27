import pyshorteners
import streamlit as st

def short_url(url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    return shortened_url

#Creando web con streamlit
st.set_page_config(page_title="URL Shortener SdeB", page_icon="/", layout="centered")
st.title("URL Shortener")
url = st.text_input("Enter the URL")
if st.button("Generate short URL"):
    st.write("URL shortened: ", short_url(url))