import streamlit as st
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
import pickle
model=pickle.load(open('estimator_pl.pkl','rb'))
st.image(r"innomatics_logo.png")
st.title("Cancer Prediction")

Age = st.number_input("Enter The Age:")
Gender =st.selectbox('Gender',['Male', 'Female'])
Tumor_Size=st.number_input('Enter The Tumor Size:')
Tumor_Grade=st.selectbox('Tumor Grade',['High','Low','Medium'])
Symptoms_Severity=st.selectbox('Symptoms Severity',['Mild', 'Moderate', 'Severe'])
Family_History = st.selectbox('Family History',['Yes','No'])
Smoking_History= st.selectbox('Smoking History',['Former Smoker', 'Current Smoker', 'Non-Smoker'])
Alcohol_Consumption=st.selectbox('Alcohol Consumption',['Moderate','High','Low'])
Exercise_Frequency = st.selectbox('Exercise Frequency',['Regularly', 'Rarely', 'Occasionally', 'Never'])

if st.button("Submit"):
    prediction=model.predict([[Age,Gender,Tumor_Size,Tumor_Grade,Symptoms_Severity,Family_History,Smoking_History,Alcohol_Consumption,Exercise_Frequency]])[0]
    if prediction==0:
        st.write('Cancer is not there')
    else:
        st.write('Cancer is there')

