# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:47:31 2025

@author: GURURAJ
"""


import pickle
import streamlit as st
import base64
from streamlit_option_menu import option_menu

# Function to set a local background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    bg_image = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(bg_image, unsafe_allow_html=True)

# Call the function with your image file path
set_background("C:/Users/btr4n/OneDrive/Desktop/ml hd/heart 13.jpg")
#"C:\Users\btr4n\OneDrive\Desktop\ml hd\heart 11.webp"
# Custom CSS for hover effect on text inputs
hover_effect = '''
<style>
.stTextInput>div>div>input:hover {
    border: 2px solid red !important;
    background-color: #ffcccb !important;
}
</style>
'''

st.markdown(hover_effect, unsafe_allow_html=True)

# Load the saved model
loaded_model = pickle.load(open("C:/Users/btr4n/OneDrive/Desktop/ml hd/trained_model.sav", 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Heart Disease Prediction'],
                           icons=['heart-pulse-fill'],
                           default_index=0)

if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST Depression')
    with col2:
        slope = st.text_input('Slope')
    with col3:
        ca = st.text_input('Higher Mean Blockages')
    with col3:
        thal = st.text_input('Type of Thalassemia')

    # Code for prediction
    heart_diagnosis = ''

    # Button for prediction
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to numerical format
            input_data = [float(age), int(sex), int(cp), float(trestbps), float(chol), 
                          int(fbs), int(restecg), float(thalach), int(exang), float(oldpeak), 
                          int(slope), int(ca), int(thal)]

            # Reshape input data for model
            input_data_reshaped = [input_data]

            # Predict
            heart_prediction = loaded_model.predict(input_data_reshaped)

            # Display result
            if heart_prediction[0] == 0:
                heart_diagnosis = "The Person Is Having Heart Disease"
            else:
                heart_diagnosis = "The Person Does Not Have Any Heart Disease"

        except ValueError:
            heart_diagnosis = "Invalid input! Please enter numeric values only."

    st.success(heart_diagnosis)

        
        
        
        
        
        
        
        
        
        
        
        
        
        