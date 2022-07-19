import streamlit as st

st.title('GEICO Claims Comprehensive Attorney Information Check-List')

claim_number = st.text_input('Enter 16 digit claim number',key = 0)
state = st.selectbox('Select state of accident',['Washington','Oregon'],key = 1)

with st.form('Claim Information',clear_on_submit = True):
  q1 = st.checkbox('No Coverage Concerns?',False)
  if state == 'Washington':
    q2 = st.checkbox('Any amount of liability accepted?',False)
    q3 = st.checkbox('No indication of big damages?',False)
    q4 = st.checkbox("2 or less IP's?", False)
    q5 = st.checkbox('No Reports of DUI or other agg liability?',False)
    st.text('No anticipated biling through:')
    harborview = st.checkbox('Harborview',False)
    Swedish = st.checkbox('Swedish',False)
    Providence = st.checkbox('Providence',False)
    Virginia_mason = st.checkbox('Virginia Mason',False)
    Valley_medical_center = st.checkbox('Valley Medical Center',False)
    hospital = ['Harborview','Swedish','Providence','Virginia Mason','Valley Medical Center']
    q6 = [harborview,Swedish,Providence,Virginia_mason,Valley_medical_center]
  elif state == 'Oregon':
    q2 = st.checkbox('Accepted 50% liability or over?',False)
    q3 = st.checkbox('No indiation of big damages?',False)
    q4 = st.checkbox("2 or less IP's?",False)
    q5 = st.checkbox('No reports of DUI or other agg liability?',False)
    q6 = st.checkbox('Consider if NPNP would apply',False)
    q7 = st.checkbox('PIP unlikely to exhaust?',False)
  submit = st.form_submit_button()

if submit == True:
  if state == 'Washington':
    st.write(f'''
    Claim Number: {claim_number}\n
    State: {state}\n
    No Coverage Concerns?: {q1}\n
    Any amount of liability accepted?: {q2}\n
    No indication of big damages?: {q3}\n
    2 or less IP's?: {q4}\n
    No Reports of DUI or other agg liability?: {q5}\n
    ''')
    if True in q6:
      st.write(f'Anticipated billing through {hospital[q6.index(True)]}')
  elif state == 'Oregon':
    st.write(f'''
    Claim Number: {claim_number}\n
    State: {state}\n
    No Coverage Concerns?: {q1}\n
    Accepted 50% liability or over?: {q2}\n
    No indiation of big damages?: {q3}\n
    2 or less IP's?: {q4}\n
    No reports of DUI or other agg liability?: {q5}\n
    Consider if NPNP would apply: {q6}\n
    PIP unlikely to exhaust?: {q7}\n
    ''')
    
 
