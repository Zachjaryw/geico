import streamlit as st
import pandas as pd
import numpy as np
from Template_Format import format

st.title('GEICO TCR II Templates')

templates = format()


st.write(templates)

template = st.selectbox('Select which template you would like to use:',list(templates.keys()))

responses = []
for i in range(len(templates[template]['Question'])):
  exec(f""" 
if {a['Condition'][i]}:
    q{i} = st.{templates[template]['Type'][i]}('{templates[template]['Question'][i]}',key = {i}{templates[template]['Addons'][i]})
    exec(f'responses.append(q{i})')
    """)
else:
    exec(f'responses.append(np.nan)')
    
if st.button('Submit'):
  for i in range(len(templates[template]['Question'])):
    exec(f"""
if not('{responses[i]}' == '{np.nan}'):
    st.write('{templates[template]['Question'][i]}: {responses[i]}')
    """)
