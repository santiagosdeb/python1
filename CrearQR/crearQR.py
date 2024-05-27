import qrcode
import qrcode.constants
import streamlit as st

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
    
st.set_page_config(page_title="SdeB Qr Code Generator", page_icon="/", layout="centered")

st.title("SdeB Qr Code Generator")
url = st.text_input("Enter the URL: ")

if st.button("Generate QR Code"):
    generate_qr_code(url,filename)
    st.image(filename,use_column_width=True)
    with open(filename,"rb") as f:
        image_data = f.read()
    download = st.download_button(label="Download QR", data=image_data, file_name="generated_qr.png")
    
    