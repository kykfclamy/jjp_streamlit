# -*- coding: utf-8 -*-
"""
Created on 21/02/2024

@author: kming
"""
import pandas as pd
import numpy as np
import base64
import streamlit as st
import datetime
##import re  #regular expressions
import json
##import redis
import os,sys

st.set_page_config(page_title='JJP - Study',  layout='wide', page_icon=':ambulance:')

dday = [12.3,12.4,12.5,12.32,11.83,12.45]

# #------------------------------------------
try:

    # dt = st.date_input('选择日期:')

    # st.write('统计日期: ', dt)

    # stk_name_df = get_stock_name()

    # stk_name_df
    
    sel_stock = st.text_input('input stockid', '600000')
    
    if sel_stock:
        st.write('stock id :', sel_stock)
        # _mkt = mkt_str(sel_stock)
        stk = mkt_str(sel_stock) + sel_stock
        
        st.write(stk)
     
        #day = get_day_quote(stk)
        
        # st.write(day)
        
        st.line_chart(data=dday, use_container_width=True)
        
    else:
        st.write('stock id :', '---')
    
    
except Exception:
    print(f'Exception: --->\
        \r\n    Function: {sys._getframe().f_code.co_name}()\
        \r\n    Line: {sys.exc_info()[-1].tb_lineno}\
        \r\n    Error: {sys.exc_info()[0]}\
        \r\n    Descript: {sys.exc_info()[1]}')
except KeyboardInterrupt:
    pass
    exit(0)
