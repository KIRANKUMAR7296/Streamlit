# Import Libraries
from numpy.testing._private.utils import IgnoreException
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from streamlit.proto.DataFrame_pb2 import Float64Index

# Title
st.write("""
# Boston House Prediction 🏠
""")

# Load Boston Dataset
boston = datasets.load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.DataFrame(boston.target, columns=['House Median Value'])

# Sidebar
st.sidebar.header('Features')


def features():
    CRIM = st.sidebar.slider('Crime Rate (per capita)', 0.00, 88.98)
    ZN = st.sidebar.slider('Residential Zone (sq.ft)', 0.00, 100.00)
    INDUS = st.sidebar.slider('Industrial Zone (sq.ft)', 0.46, 27.74)
    CHAS = st.sidebar.slider('Charles River', 0.00, 1.00)
    NOX = st.sidebar.slider('Nitrogen Oxide Concentration', 0.38, 0.87)
    RM = st.sidebar.slider('Average Number of Rooms', 3.56, 8.78)
    AGE = st.sidebar.slider('Age of House', 2.90, 100.00)
    DIS = st.sidebar.slider(
        'Distance from 5 Boston Employment Centres', 1.12, 12.12)
    RAD = st.sidebar.slider('Accessibility to Radial Highways', 1.00, 24.00)
    TAX = st.sidebar.slider('Property Tax Rate ($)', 187.00, 771.00)
    PTRATIO = st.sidebar.slider('Pupil Teacher Ratio', 12.60, 22.00)
    B = st.sidebar.slider('Proportion of Blacks', 0.32, 396.90)
    LSTAT = st.sidebar.slider('Lower Status of Population (%)', 1.73, 37.97)
    data = {'CRIM': CRIM,
            'ZN': ZN,
            'INDUS': INDUS,
            'CHAS': CHAS,
            'NOX': NOX,
            'RM': RM,
            'AGE': AGE,
            'DIS': DIS,
            'RAD': RAD,
            'TAX': TAX,
            'PTRATIO': PTRATIO,
            'B': B,
            'LSTAT': LSTAT}
    features = pd.DataFrame(data, index=[0])
    return features


df = features()

st.header('Features')
st.write(df)

# Data Description
data = {
    'Data': ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'BLACK', 'LSTAT', 'MEDV'],
    'Description': ['Crime Rate', 'Residential Zone', 'Industrial Zone', 'Charles River', 'Nitrogen Oxide Concentration', 'Average Number of Rooms', 'Age of House', 'Distance to 5 Boston Employment Centres', 'Accessibility to Radial Highways', 'Property Tax Rate', 'Pupil Teacher Ratio', 'Proportion of Black', 'Lower Status of Population', 'Median Value of Owner Occupied Homes']
}

description = pd.DataFrame(data)

st.subheader('Data Description')
st.write(description)

# Import Model
model = pickle.load(open('Regression_Model.pkl', 'rb'))

# Make Prediction
st.header('Prediction')
st.write(f'Median Value of Owner Occupied Home : {model.predict(df)}')
