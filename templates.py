import streamlit as st
import pandas as pd
import numpy as np
from Template_Format import format
st.title('GEICO TCR II Templates')
templates = format()
template = st.selectbox('Select which template you would like to use:',list(templates.keys()))
responses = []
for i in range(len(templates[template]['Question'])):
  reverse == False
  if templates[template]['Condition'][i] == True:
    check = True
  else:
    if 'N' in templates[template]['Condition'][i]:
      reverse == True
      check = responses[int(templates[template]['Condition'][i][1:])]
    else:
      check = responses[int(templates[template]['Condition'][i])]
  st.write(check)
  st.write(responses)
  if check == True or check == 'Y' or (reverse == True and check == 'N'):
    exec(f"""q{i} = st.{templates[template]['Type'][i]}('{templates[template]['Question'][i]}',key = {i}{templates[template]['Addons'][i]})""")
    exec(f"""
if q{i} == True:
 q{i} = 'Y'
elif q{i} == False:
  q{i} = 'N'
exec(f'responses.append(q{i})')
    """)
else:
    exec(f'responses.append(np.nan)') 
if st.button('Submit'):
  for i in range(len(templates[template]['Question'])):
    if not(responses[i] == np.nan):
      exec(f"""st.write('{templates[template]['Question'][i]}: {responses[i]}')""")
