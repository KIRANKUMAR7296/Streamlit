# Import Libraries
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

# Title
st.write('''
# Iris Flower Prediction 🌻
''')

# Sidebar
st.sidebar.header('Features')


def features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)
    data = {
        'Sepal Length': sepal_length,
        'Sepal Width': sepal_width,
        'Petal Length': petal_length,
        'Petal Width': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features


df = features()
st.subheader('Features')
st.write(df)

iris = datasets.load_iris()
X = iris.data
y = iris.target

# Import Model
clf = pickle.load(open('Iris_Classification.pkl', 'rb'))

# Class Labels
label_names = {'Flower Species': ['Setosa', 'Versicolor', 'Virginica']}
df_label = pd.DataFrame(label_names)
st.subheader('Class Labels')
st.write(df_label)

# Prediction Probability
st.subheader('Prediction Probability')
st.write(clf.predict_proba(df))

# Predict Species of Flower
if clf.predict(df) == 0:
    species = 'Flower is Setosa 🌸'
elif clf.predict(df) == 1:
    species = 'Flower is Versicolor 🌸'
else:
    species = 'Flower is Virginica 🌸'

st.subheader('Species 🌻')
st.write(species)
