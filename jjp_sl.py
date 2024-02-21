# -*- coding: utf-8 -*-
"""
Created on 21/02/2024

@author: kming
"""
import pandas as pd
import numpy as np
import base64
import streamlit as st
from streamlit.components.v1 import html
import datetime
##import re  #regular expressions
import json
##import redis
import os,sys

st.set_page_config(page_title='JJP - Study',  layout='wide', page_icon=':ambulance:')

# dday = np.array([12.3,12.4,12.5,12.32,11.83,12.45])

# #------------------------------------------
try:

    # dt = st.date_input('选择日期:')

    # st.write('统计日期: ', dt)

    # stk_name_df = get_stock_name()

    # stk_name_df
    
    sel_stock = st.text_input('input stockid', '600000')

    # st.line_chart(data=dday, use_container_width=True)

    st.line_chart(data=np.random.rand(50), use_container_width=True)
    
except Exception:
    print(f'Exception: --->\
        \r\n    Function: {sys._getframe().f_code.co_name}()\
        \r\n    Line: {sys.exc_info()[-1].tb_lineno}\
        \r\n    Error: {sys.exc_info()[0]}\
        \r\n    Descript: {sys.exc_info()[1]}')
except KeyboardInterrupt:
    pass
    exit(0)

st.markdown(
    r"""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    .viewerBadge_container__r5tak {display: none;}
    .styles_viewerBadge__CvC9N {display: none;}
    </style>
    """, unsafe_allow_html=True
)

html(r"""
    <script>
    window.setTimeout(function (){
        document.getElementsByClassName("viewerBadge_container__r5tak")[0].remove();
    }, 5000);
    </script>
""")
