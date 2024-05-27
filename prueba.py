import qrcode
import qrcode.constants
import pyshorteners
import streamlit as st
import re

filename = "./qr_code.png"

def generate_qr_code(url,filename):
    qr = qrcode.QRCode(
        version= 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def short_url(url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    return shortened_url

def link_validator(url):
    pattern = r'^(https?:\/\/)?[\w\-]+(\.[\w\-]+)+[/#?]?.*$'

    if re.match(pattern, url):
        return True
    else:
        return False

st.set_page_config(page_title="SdeB Python", page_icon="/", layout="centered")
st.title("QR creator & Link Shortener")
c1,c2 = st.columns(2)
c1.subheader("Generate your QR!")
url = c1.text_input("Enter the URL: ")

if c1.button("Generate QR Code"):
    if not url:
        c1.warning("Enter a url")
    elif not link_validator(url):
        c1.warning("Enter a valid url")
    else:
        generate_qr_code(url,filename)
        c1.image(filename,use_column_width=True)
        with open(filename,"rb") as f:
            image_data = f.read()
        download = c1.download_button(label="Download QR", data=image_data, file_name="generated_qr.png")
    
c2.subheader("URL Shortener")
url2 = c2.text_input("Enter the URL")
if c2.button("Generate short URL"):
    if not url2:
        c2.warning("Enter a url")
    elif not link_validator(url2):
        c2.warning("Enter a valid url")
    else:
        link_validator(url2)
        url_shortened = short_url(url2)
        c2.write(f"URL shortened: {url_shortened}")