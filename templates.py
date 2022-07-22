import streamlit as st
import pandas as pd
import numpy as np
from Template_Format import format

st.title('GEICO TCR II Templates')

templates = format()

st.write(templates)
