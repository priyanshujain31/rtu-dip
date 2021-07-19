import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras.preprocessing import image
import os
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)
from keras.models import load_model

html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing lab</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
         Mathematical Operations on Images
         """
         )
file= st.file_uploader("Please upload image", type=("jpg", "png"))
Operation = st.selectbox(
    "operation",
    ("-","/")
    )

import cv2
from  PIL import Image, ImageOps
def import_and_predict(img3,Operation):
  
  img4=np.ones(img3.shape, dtype="uint8")*100 
  if Operation=='-':
    img5=img3-img4
  if Operation=='/':
    img5=img3/img4
  st.image(img5, use_column_width=True)
  return 0

if file is None:
  st.text("Please upload an Image file")
else:
  file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, 1)
  st.image(file,caption='Uploaded Image.', use_column_width=True)
    
if st.button("perform"):
  result=import_and_predict(image,Operation)
  
if st.button("About"):
  st.header(" Priyanshu Jain")
  st.subheader("C-Section ,PIET")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Digital Image processing </p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)