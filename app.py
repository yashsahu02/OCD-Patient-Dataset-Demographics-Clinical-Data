import streamlit as st 

import numpy as np
import pandas as pd
import pickle

st.set_page_config(
    page_title = "OCD Patient Medication Prediction",
    page_icon="💊"
)

st.title('OCD Patient Medication Prediction')

model = pickle.load(open('models/model.pkl','rb'))
df = pickle.load(open('models/dataframe.pkl','rb'))
preprocessor = pickle.load(open('models/preprocessor.pkl','rb'))


company_list = df['Company'].unique()
selected_company = st.selectbox(
    'Select Company',
    company_list,
)


product_dict = df.groupby('Company')['Product'].unique().to_dict()
product_list = product_dict[selected_company]

selected_product = st.selectbox(
    'Select Product',
    product_list
)

type_dict = df.groupby('Company')['TypeName'].unique().to_dict()
type_list = type_dict[selected_company]

selected_typeName = st.selectbox(
    'Select Type',
    type_list
)

selected_inches = st.selectbox(
    'Screen Size in Inches',
    sorted(list(set(df['Inches'])))
)


selected_ram = st.selectbox(
    'Select RAM Size',
    sorted(list(set(df['Ram'])))
)

os_dict = df.groupby('Company')['OS'].unique().to_dict()
os_list = os_dict[selected_company]
selected_os = st.selectbox(
    'Select OS',
    os_list
)

selected_weight = st.selectbox(
    'Select Weight',
    sorted(list(set(df['Weight'])))
)

selected_screen_type = st.selectbox(
    'Select Screen Type',
    sorted(list(set(df['Screen'])))
)

selected_ScreenW = st.selectbox(
    'Select ScreenW',
    sorted(list(set(df['ScreenW'])))
)

selected_ScreenH = st.selectbox(
    'Select ScreenH',
    sorted(list(set(df['ScreenH'])))
)

selected_Touchscreen = st.selectbox(
    'Touchscreen',
    df['Touchscreen'].unique()
)

selected_IPSpanel = st.selectbox(
    'IPSpanel',
    df['IPSpanel'].unique()
)

selected_RetinaDisplay = st.selectbox(
    'RetinaDisplay',
    df['RetinaDisplay'].unique()
)

CPU_company_dict = df.groupby('Company')['CPU_company'].unique().to_dict()
CPU_company_list = CPU_company_dict[selected_company]
selected_CPU_company = st.selectbox(
    'Select CPU Comapny',
    CPU_company_list
)
