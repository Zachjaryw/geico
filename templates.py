import streamlit as st
import pandas as pd
import numpy as np
from Template_Format import format

st.title('GEICO TCR II Templates')

templates = format()

#st.write(templates)


a = {'Question':['How are you?','Are you a human?','How many?'],
    'Type':['text_input','checkbox','number_input'],
    'Addons':['',',value = False',',min_value = 1, max_value = 10,step = 1'],
    'Condition':[True,True,'responses[1]']}

responses = []
for i in range(len(a['Question'])):
  exec(f""" 
if {a['Condition'][i]}:
    q{i} = st.{a['Type'][i]}('{a['Question'][i]}',key = {i}{a['Addons'][i]})""")
    exec(f'responses.append(q{i})')
else:
    exec(f'responses.append(np.nan)')
    
if st.button('Submit'):
  for i in range(len(a['Question'])):
    exec(f"st.write('{a['Question'][i]}: {responses[i]}')")
