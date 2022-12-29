import streamlit as st

folder_prefix = "images/"
images_meta = [
    {'filename': "alpha.png"},
    {'filename': "bgra.png"},
    {'filename': "blue.png"},
    {'filename': "circle.gif"},
    {'filename': "gray.png"},
    {'filename': "green.png"},
    {'filename': "image.jpeg"},
    {'filename': "image.png"},
    {'filename': "pseudorandom.png"},
    {'filename': "red.png"},
]

images = []
captions = []

for meta in images_meta:
    images.append(folder_prefix + meta['filename'])
    captions.append(meta['filename'])

st.image(images, caption=captions)
