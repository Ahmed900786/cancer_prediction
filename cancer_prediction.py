import streamlit as st
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
import pickle
model=pickle.load(open('estimator_pl.pkl','rb'))
st.image(r'innomatics_logo.png')
st.title("Cancer Prediction")

Age = st.number_input("Enter The Age:")
Gender =st.text_input('Enter The Gender:')
Tumor_Size=st.number_input('Enter The Tumor Size:')
Tumor_Grade=st.text_input('Enter The Tumor Grade:')
Symptoms_Severity=st.text_input('Enter The Tumor Symptoms Severity:')
Family_History = st.text_input('Enter The Family History:')
Smoking_History= st.text_input('Enter The Smoking History:')
Alcohol_Consumption=st.text_input('Enter The Alcohol Consumption:')
Exercise_Frequency = st.text_input('Enter The Excercise Frequency:')

if st.button("Submit"):
    prediction=model.predict([[Age,Gender,Tumor_Size,Tumor_Grade,Symptoms_Severity,Family_History,Smoking_History,Alcohol_Consumption,Exercise_Frequency]])[0]
    if prediction==0:
        st.write('Cancer is not there')
    else:
        st.write('Cancer is there')

