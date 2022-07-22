import streamlit as st
import pandas as pd
import numpy as np
from Template_Format import format

st.title('GEICO TCR II Templates')

templates = format()

#st.write(templates)


a = {'Question':['How are you?','Are you a human?','How many?'],
    'Type':['text_input','checkbox','number_input'],
    'Addons':['',',value = False',',min = 1, max = 10']}

responses = []
for i in range(len(a['Question'])):
  exec(f"q{i} = st.{a['Type'][i]}({a['Question'][i]},key = {i}{a['Addons'][i]})")
  exec(f'responses.append(q{i})')
  
if st.button('Submit'):
  for i in range(len(a['Question'])):
    exec(f"st.write({a['Question'][i]}: {responses[i]})")
