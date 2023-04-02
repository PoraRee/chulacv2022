# import libraries
from PIL import Image
import streamlit as st
import requests
import base64
from io import BytesIO
import json

# set title of app

st.title("Chest X-Ray Classification Application")
st.write("")

# enable users to upload images for the model to make predictions
file_up = st.file_uploader("Upload an image", type = ["jpg","jpeg","png",'webp'])


def predict(image):
    url = 'http://0.0.0.0:8500/chestxray'
    byte_io = BytesIO()
    image.save(byte_io, 'png')
    byte_io.seek(0)
    x = requests.post(url, files={
        'image': (
            '1.png',
            byte_io,
            'multipart/form-data'
        )
    },)
    
    return x.text

if file_up is not None:
    # display image that user uploaded
    image = Image.open(file_up).convert('RGB')
    st.image(image, caption = 'Uploaded Image.', use_column_width = True)
    st.write("")
    st.write("Just a second ...")
    labels = predict(image)
    st.write('Predict: ',labels)

