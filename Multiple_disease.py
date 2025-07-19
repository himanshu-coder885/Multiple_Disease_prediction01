import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading _model
heart_disease_prediction = pickle.load(open("C:/Users/A/Desktop/Multipple Disease/Model/Heart_disease_model.sav",'rb'))

diabetes_model  = pickle.load(open("C:/Users/A/Desktop/Multipple Disease/Model/diabetes (1).sav",'rb'))



#sidebar for navigation
with st.sidebar:
   selected = option_menu(
    'Multiple Disease Prediction System', 
    ['Heart Disease Prediction','Diabetes Prediction'],
    icons=['heart','activity'], 
    default_index=0
)

if (selected == 'Heart Disease Prediction'):
   st.title('Heart Disease Prediction')
   
   col1, col2, col3 = st.columns(3)

   with col1:
      age = st.text_input('Age')
   with col2:
      sex = st.text_input('sex')    
   with col3:    
      cp = st.text_input('Chest pain types')
   with col1:
      trestbps = st.text_input('Resting Blood Pressure')
   with col2:
      chol = st.text_input('Serum Cholestrol in mg/dL')
   with col3:
      fbs = st.text_input('Fasting Blood sugur > 120 mg/dL')   
   with col1:
      restecg = st.text_input('Resting Electrocardiographic result')
   with col2:
      thalach = st.text_input('Maximum Heart Rate achieved')
   with col3:
      exang = st.text_input("Exercise Induced Angina")
   with col1:
      oldpeak = st.text_input("ST depression induced by exercise")
   with col2:
      slope = st.text_input("Slop of the peak exercise ST segment")
   with col3:
      ca = st.text_input("Major vessels colored by flourosopy")
   with col1:
      thal = st.text_input("thal : normal = 0; fixed defect = 1; reversable defect = 2;")   

# Code for Prediction
   heart_diagnosis = ''

   if st.button('Heart disease Test result'):
   
    heart_prediction = heart_disease_prediction.predict([[age, sex, cp,
                                               trestbps, chol, fbs,
                                               restecg, thalach,exang,oldpeak,slope,ca,thal]])
    
    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person is not have any heart disease'

 
    st.success(heart_diagnosis)


if (selected == 'Diabetes Prediction'):
   st.title('Diabetes Prediction System ')

   col1 , col2, col3 = st.columns(3)

   with col1:
      Pregnancies = st.text_input('Number of Pregnancies')
   with col2:
      Glucose = st.text_input('Glucose Level')    
   with col3:    
      BloodPressure = st.text_input('Blood Pressure value')
   with col1:
      SkinThickness = st.text_input('Skin Thickness value')
   with col2:
      Insulin = st.text_input('Insulin Level')
   with col3:
      BMI = st.text_input('BMI value')   
   with col1:
      DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
   with col2:
      Age = st.text_input('Age of the person')

# Code for Prediction
   diab_diagnosis = ''

   if st.button('Diabetes Test result'):
    # Jab button click hoga tabhi prediction chalega-
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,
                                               SkinThickness, Insulin, BMI,
                                               DiabetesPedigreeFunction, Age]])
    
    if diab_prediction[0] == 1:
        diab_diagnosis = 'The person is Diabetic'
    else:
        diab_diagnosis = 'The person is Not Diabetic'

    # Show result only after button click
    st.success(diab_diagnosis)
