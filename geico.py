import streamlit as st
from Dropbox_Setup import * #access dropbox
import pandas as pd
import numpy as np

st.title('GEICO Claims Comprehensive Attorney Information Check-List')

def reset(dbx):
  toDBX(dbx,{'Claim Number':[],
             'State':[],
             'ECR Eligable':[],
             'Question Responses':[],
             'Additional Information':[]},st.secrets.filepath.rentonCAIC)


dbx = initializeToken(st.secrets.Token.token)
data = fromDBX(dbx,st.secrets.filepath.rentonCAIC)

claim_number = st.text_input('Enter 16 digit claim number',key = 0)
state = st.selectbox('Select state of accident',['Washington','Oregon'],key = 1)
with st.container():
  q1 = st.checkbox('No Coverage Concerns?',False)
  if state == 'Washington':
    q2 = st.checkbox('Any amount of liability accepted?',False)
    q3 = st.checkbox('No indication of big damages?',False)
    q4 = st.checkbox("2 or less IP's?", False)
    q5 = st.checkbox('No Reports of DUI or other agg liability?',False)
    st.text('Anticipated biling through:')
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

  if state == 'Oregon' and not(False in [q1,q2,q3,q4,q5,q6,q7]):
    q8 = True
  elif state == 'Washington' and not(False in [q1,q2,q3,q4,q5]) and not(True in q6):
    q8 = True
  else:
    q8 = False

  if q8 == True:
    q9 = st.text_input('BI Limits:',key = 2)
    q10 = st.number_input('Number pf BI exposures:',key = 3,step = 1,min_value = 0)
    q11 = st.checkbox('Police report for the loss in file?',False)
    if q11 == True:
      q11_1 = st.text_input('Injuries mentioned?',key = 4)
    q12 = st.checkbox('Claimant photos on file?',False)
    q13 = st.checkbox('Insured photos on file?', False)
    q14 = st.text_input('Liabilty percentage?',key = 5)
    q15 = st.text_input('Accident type:',key = 6)
    q16 = st.checkbox('Claimant BI RI on file?',False)
    q17 = st.checkbox('Has attorney provided injury information?',False)
    q18 = st.checkbox('Insured RI to determine impact serverity, injuries of insd/clmt?',False)

  col1, col2 = st.columns(2)
  
  additional_info = col1.button('Submit And Add Additoinal Information')
  submit = col2.button('Submit Without Additoinal Information')

if submit == True:
  printvalue = ''
  if state == 'Washington':
    printvalue = printvalue + f'''
    Claim Number: {claim_number}\n
    State: {state}\n
    No Coverage Concerns?: {q1}\n
    Any amount of liability accepted?: {q2}\n
    No indication of big damages?: {q3}\n
    2 or less IP's?: {q4}\n
    No Reports of DUI or other agg liability?: {q5}\n
    '''
    if True in q6:
      printvalue = printvalue + f'Anticipated billing through {hospital[q6.index(True)]}'
    printvalue = printvalue + f'Claim is ECR eligable?: {q8}'
    if q8 == True:
      printvalue = printvalue + f'''
      BI Limits: {q9}\n
      Number pf BI exposures: {q10}\n
      Police report for the loss in file?: {q11}\n
      '''
      if q11 == True:
        printvalue = printvalue + f'\tInjuries mentioned?: {q11_1}\n'
      printvalue = printvalue + f'''
      Claimant photos on file?: {q12}\n
      Insured photos on file?: {q13}\n
      Liabilty percentage?: {q14}\n
      Accident type: {q15}\n
      Claimant BI RI on file?: {q16}\n
      Has attorney provided injury information?: {q17}\n
      Insured RI to determine impact serverity, injuries of insd/clmt?: {q18}\n
      '''
  elif state == 'Oregon':
    printvalue = printvalue + f'''
    Claim Number: {claim_number}\n
    State: {state}\n
    No Coverage Concerns?: {q1}\n
    Accepted 50% liability or over?: {q2}\n
    No indiation of big damages?: {q3}\n
    2 or less IP's?: {q4}\n
    No reports of DUI or other agg liability?: {q5}\n
    Consider if NPNP would apply: {q6}\n
    PIP unlikely to exhaust?: {q7}\n
    Is this claim offer ECR eligable?: {q8}\n
    '''
    if q8 == True:
      printvalue = printvalue + f'''
      BI Limits: {q9}\n
      Number pf BI exposures: {q10}\n
      Police report for the loss in file?: {q11}\n
      '''
      if q11 == True:
        printvalue = printvalue + f'\tInjuries mentioned?: {q11_1}\n'
      printvalue = printvalue + f'''
      Claimant photos on file?: {q12}\n
      Insured photos on file?: {q13}\n
      Liabilty percentage?: {q14}\n
      Accident type: {q15}\n
      Claimant BI RI on file?: {q16}\n
      Has attorney provided injury information?: {q17}\n
      Insured RI to determine impact serverity, injuries of insd/clmt?: {q18}\n
      '''
  st.write(printvalue)
  data['Claim Number'].append(claim_number)
  data['State'].append(state)
  data['ECR Eligable'].append(q8)
  data['Question Responses'].append(printvalue)
  data['Additional Information'].append('None')
  toDBX(dbx,data,st.secrets.filepath.rentonCAIC)
elif additional_info == True:
  printvalue = ''
  if state == 'Washington':
    printvalue = printvalue + f'''
    Claim Number: {claim_number}\n
    State: {state}\n
    No Coverage Concerns?: {q1}\n
    Any amount of liability accepted?: {q2}\n
    No indication of big damages?: {q3}\n
    2 or less IP's?: {q4}\n
    No Reports of DUI or other agg liability?: {q5}\n
    '''
    if True in q6:
      printvalue = printvalue + f'Anticipated billing through {hospital[q6.index(True)]}'
    printvalue = printvalue + f'Claim is ECR eligable?: {q8}'
    if q8 == True:
      printvalue = printvalue + f'''
      BI Limits: {q9}\n
      Number pf BI exposures: {q10}\n
      Police report for the loss in file?: {q11}\n
      '''
      if q11 == True:
        printvalue = printvalue + f'\tInjuries mentioned?: {q11_1}\n'
      printvalue = printvalue + f'''
      Claimant photos on file?: {q12}\n
      Insured photos on file?: {q13}\n
      Liabilty percentage?: {q14}\n
      Accident type: {q15}\n
      Claimant BI RI on file?: {q16}\n
      Has attorney provided injury information?: {q17}\n
      Insured RI to determine impact serverity, injuries of insd/clmt?: {q18}\n
      '''
  elif state == 'Oregon':
    printvalue = printvalue + f'''
    Claim Number: {claim_number}\n
    State: {state}\n
    No Coverage Concerns?: {q1}\n
    Accepted 50% liability or over?: {q2}\n
    No indiation of big damages?: {q3}\n
    2 or less IP's?: {q4}\n
    No reports of DUI or other agg liability?: {q5}\n
    Consider if NPNP would apply: {q6}\n
    PIP unlikely to exhaust?: {q7}\n
    Is this claim offer ECR eligable?: {q8}\n
    '''
    if q8 == True:
      printvalue = printvalue + f'''
      BI Limits: {q9}\n
      Number pf BI exposures: {q10}\n
      Police report for the loss in file?: {q11}\n
      '''
      if q11 == True:
        printvalue = printvalue + f'\tInjuries mentioned?: {q11_1}\n'
      printvalue = printvalue + f'''
      Claimant photos on file?: {q12}\n
      Insured photos on file?: {q13}\n
      Liabilty percentage?: {q14}\n
      Accident type: {q15}\n
      Claimant BI RI on file?: {q16}\n
      Has attorney provided injury information?: {q17}\n
      Insured RI to determine impact serverity, injuries of insd/clmt?: {q18}\n
      '''
  with st.form('Additional Info'):
    add_0 = st.text_input('Name of spouse or domestic partner')
    add_1 =st.text_input('Treatment Status Update')
    add_2 =st.text_input('Medicare, Medicaid, ERISA, Tricare eligable?')
    add_3 =st.text_input('Estimated Treatment Timeframe')
    add_4 =st.text_input('Dx of Injuries (diagnosis)')
    add_5 =st.text_input('Diagnosic testing done')
    add_6 =st.text_input('Loss of Wages')
    add_7 =st.text_input('Missed life events/daily activities')
    add_8 =st.text_input('County/Venue of Accident')
    formSubmit = st.form_submit_button()
    
  if formSubmit:
    additionalInformation = f'''
    Name of spouse or domestic partner: {add_0}\n
    Treatment Status Update: {add_1}\n
    Medicare, Medicaid, ERISA, Tricare eligable?: {add_2}\n
    Estiamted Treatment Timeframe: {add_3}\n
    Dx of Injuries (diagnosis): {add_4}\n
    Diagnosic testing done: {add_5}\n
    Loss of Wages: {add_6}\n
    Missed life events/daily activities: {add_7}\n
    County/Venue of Accident: {add_8}\n
    '''
    st.write(printvalue,'\n',additionalInformation)
    data['Claim Number'].append(claim_number)
    data['State'].append(state)
    data['ECR Eligable'].append(q8)
    data['Question Responses'].append(printvalue)
    data['Additional Information'].append(additionalInformation)
    toDBX(dbx,data,st.secrets.filepath.rentonCAIC)
