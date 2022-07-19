import streamlit as st

st.title('GEICO Claims Comprehensive Attourney Information Check-List')

claim_number = st.text_input('Enter 16 digit claim number',key = 0)

state = st.select_box(['Washington','Oregon'],key = 1)

if state == 'Oregon':
  st.write('Oregon')
elif state == 'Washington':
  st.write('Washington')
