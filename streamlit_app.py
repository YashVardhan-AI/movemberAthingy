import streamlit as st
from utils import ctscanutils, xrayutils
from PIL import Image

st.set_page_config(page_title='covid detection', layout= 'wide')

st.title('covid detection')
st.sidebar.title('Navigation')

page = st.sidebar.selectbox("Select page:", options = ["Welcome", "xray", "ctscan"])

if page == 'Welcome':
    st.markdown("### Please select the page you want to navigate to.")
    st.markdown("""
    - xray: you can use a lung xray to detect covid-19 or pnemonia
    - ctscan: you can use a chest ctscan to detect covid-19
    it is recommended to use the xray first, then ctscan if you have a lung ctscan to use. 
                """)
    st.markdown("it is not a replacement for a docter, it is just to help you to detect covid-19 or pnemonia based on input images and can be horribaly inacurate(though usually its not too bad).")

elif page == 'xray':
    content = st.sidebar.file_uploader("upload a xray image of your lung", type=['png', 'jpg', 'jpeg'])
    if content is not None:
        image = Image.open(content).convert('RGB')
        pred= xrayutils.prediction(image)
        st.image(image, width=600)
        st.warning("the prediction is: " + pred)
    else:
        st.warning("please upload a xray image of your lung")

elif page == 'ctscan':
    content = st.sidebar.file_uploader("upload a ctscan image of your chest", type=['png', 'jpg', 'jpeg'])
    if content is not None:
        image = Image.open(content).convert('RGB')
        pred= ctscanutils.prediction(image)
        st.image(image, width=600)
        st.warning("the prediction is: " + pred)
        
    else:
        st.warning("please upload a ctscan image of your chest")