import streamlit as st
from Dropbox_Setup import * #access dropbox
import pandas as pd
import numpy as np
import datetime as dt

st.title('GEICO Claims ECR Add On Template')

def reset(dbx):
  toDBX(dbx,{'Date':[],
             'Claim Number':[],
             'Injured Parties Name':[],
             'State':[],
             'ECR Eligible':[],
             'Reported Offer Made':[],
             'Reported Claim Settled':[],
             'Question Responses':[]},st.secrets.filepath.rentonCAIC)

dbx = initializeToken(st.secrets.Token.token)
  
data = fromDBX(dbx,st.secrets.filepath.rentonCAIC)

claim_number = st.text_input('Enter 16 digit claim number',key = 0)
if claim_number != st.secrets.override.dataoverride and claim_number != st.secrets.override.resetoverride:
  df = pd.DataFrame(data)
  df = df[df['Claim Number'] == claim_number]
  if df.empty ==  True:
    existingnames = []
  else:
    existingnames = df['Injured Parties Name'].tolist()
  selectname = st.selectbox("Select IP's Name:",['---Select One---','New Injured Party'] + existingnames,key = 40)
  if selectname == '---Select One---':
    st.warning('Select an injured party or create new injured party report')
  elif selectname == 'New Injured Party':
    name = st.text_input('Injured Parties Name')
    if name in existing names:
      st.warning('This individual has an existing ECR Report. Please select their name in the dropdown.')
    else:
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
          q3 = st.checkbox('No indication of big damages?',False)
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
          q9 = st.selectbox('BI Limits:',['25/50','50/100','100/200','100/300','300/300','300/500'],key = 2)
          q10 = st.number_input('Number of BI exposures:',key = 3,step = 1,min_value = 1)
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
        submit = st.button('Submit')

      if submit == True:
        if q8 == True:
          if q9 == '25/50':
            max_payout = round(50000/q10,2)
            if max_payout > 25000:
              max_payout = 25000
            max_payout = "${:.2f}".format(max_payout)
          elif q9 == '50/100':
            max_payout = round(100000/q10,2)
            if max_payout > 50000:
              max_payout = 50000
            max_payout = "${:.2f}".format(max_payout)
          elif q9 == '100/200':
            max_payout = round(200000/q10,2)
            if max_payout > 100000:
              max_payout = 100000
            max_payout = "${:.2f}".format(max_payout)
          elif q9 == '100/300':
            max_payout = round(300000/q10,2)
            if max_payout > 100000:
              max_payout = 100000
            max_payout = "${:.2f}".format(max_payout)
          elif q9 == '300/300':
            max_payout = round(300000/q10,2)
            if max_payout > 300000:
              max_payout = 300000
            max_payout = "${:.2f}".format(max_payout)
          elif q9 == '300/500':
            max_payout = round(500000/q10,2)
            if max_payout > 300000:
              max_payout = 300000
            max_payout = "${:.2f}".format(max_payout)
        printvalue = ''
        printvalue = printvalue + f'''
    Claim Number: {claim_number}\n
    State: {state}\n
    Injured Parties Name: {name}\n'''
        ECREligable = ''
        if q8 == True:
          hes = False
          if (False in [q12,q13]):
            ECREligable += ' Additional Accident Images Req (F/U).'
            hes = True
          if (False in [q16,q17,q18]):
            ECREligable += ' Additional Injury Information Req (F/U).'
            hes = True
          if hes == True:
            ECREligable = f'Claim is ECR eligible?: Possible.' + ECREligable
          elif hes == False:
            ECREligable = f'Claim is ECR eligible?: True' + ECREligable
        else:
          ECREligable += f'Claim is ECR eligible?: {q8}'
        printvalue =  printvalue + '\n' + ECREligable + '\n'
        if state == 'Washington':
          rec_payout = "${:.2f}".format(7000)
          printvalue = printvalue + f'''
    No Coverage Concerns?: {q1}\n
    Any amount of liability accepted?: {q2}\n
    No indication of big damages?: {q3}\n
    2 or less IP's?: {q4}\n
    No Reports of DUI or other agg liability?: {q5}\n
          '''
          if True in q6:
            printvalue = printvalue + f'Anticipated billing through {hospital[q6.index(True)]}'

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
    Has attorney provided injury information? (if not repped, set to true): {q17}\n
    Insured RI to determine impact serverity, injuries of insd/clmt?: {q18}\n
    \n\n
    Maximum Tender Per Claimant: {max_payout}\n
    Recommended ECR Tender Per Claimant: {rec_payout}\n
            '''
        elif state == 'Oregon':
          rec_payout = "${:.2f}".format(3500)
          printvalue = printvalue + f'''
    No Coverage Concerns?: {q1}\n
    Accepted 50% liability or over?: {q2}\n
    No indication of big damages?: {q3}\n
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
    \n\n
    Maximum Tender Per Claimant: {max_payout}\n
    Recommended ECR Tender Per Claimant: {rec_payout}\n
            '''

        st.write(printvalue)

        data['Date'].append(str(dt.date.today()))
        data['Claim Number'].append(claim_number)
        data['State'].append(state)
        data['ECR Eligible'].append(ECREligable)
        data['Question Responses'].append(printvalue)
        data['Reported Offer Made'].append("COLLECT FROM ATLAS")
        data['Reported Claim Settled'].append("COLLECT FROM ATLAS")
        data['Injured Parties Name'].append(name)

        toDBX(dbx,data,st.secrets.filepath.rentonCAIC)

  elif selectname in existingnames:
    df = pd.DataFrame(data)
    df = df[df['Claim Number'] == claim_number]
    pos = df[df['Injured Parties Name'] == selectname]
    pos = list(pos.index)
    st.write(pos)
  
  
  
elif claim_number == st.secrets.override.dataoverride:
  df = pd.DataFrame(data)
  st.dataframe(df)
elif claim_number == st.secrets.override.resetoverride:
  toreset = st.text_input('To Reset Type "Reset CAIC Data"')
  if toreset == 'Reset CAIC Data':
    reset(dbx)
