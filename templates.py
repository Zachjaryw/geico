import streamlit as st
import pandas as pd
import numpy as np
from Template_Format import format
st.title('GEICO TCR II Templates')
templates = format()
template = st.selectbox('Select which template you would like to use:',list(templates.keys()))
responses = []
for i in range(len(templates[template]['Question'])):
  if templates[template]['Condition'][i] == True:
    check = True
  else:
    if 'N' in templates[template]['Condition'][i]:
      check = responses[int(templates[template]['Condition'][i][1:])]
      if check == 'N':
        check = 'Y'
      else:
        check == 'N'
    else:
      check = responses[int(templates[template]['Condition'][i])]
  st.write(check)
  st.write(responses)
  if check == True or check == 'Y':
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
