# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 00:54:29 2024

@author: HP
"""

import streamlit as st
import joblib


def main():
    
    #model_path = r'C:\Users\HP\path\to\your\model'
    #model = joblib.load(C:\Users\HP\OilViscosity1Model_rf)
    
    html_temp = """
    <div style= "background-color:blue; padding:12px; border: 3px solid white; border-radius: 10px">
    <h2 style = "color:white; text-align:center; font-family: 'Arial', sans-serif">Predicting Viscosity Status, Percentage, Test Result</h2> 
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    
    model = joblib.load('OilViscosity1Model_rf_100_40.joblib')  
    
    Visc_temp = st.selectbox('Select Viscosity Temperature you want to Predict on:' ,options =['40°C', '100°C'])
        
    p2 = st.selectbox('Select the Year you want to Predict (Possible for past and future as well):' ,options =[2021, 2022, 2023, 2024, 2025])
    
    p3 = st.slider("Select the month you want to Predict:",1,12)
    
    p4 = st.number_input("Select the Date you want to Predict:", step=1, format="%d", value = 1, max_value=31)
    
   
    
    if Visc_temp == '100°C':
        p1 = 100
    else:
        p1 = 40
    
    
    if p1 == 100:
        OilStandard = 15.3
    else:
        OilStandard = 115
    
    
    pred = model.predict([[p1,p2,p3,p4]])
    pred_value = round(pred[0], 2)
    
    Viscosity = ((pred_value / OilStandard) - 1) * 100
    ViscosityPct = round(Viscosity, 2)
        
    if st.button("Predict"):
        
        # Determine the status based on the prediction value 
        if -10 <= ViscosityPct <=10:
            status = 'Normal'
        elif -30 <= ViscosityPct <= 30:
            status = 'Warning'
        else:
            status = 'Problem'
        
        st.success(f'Predicted Value of Oil Viscosity% on {p4}/{p3}/{p2} will be : {ViscosityPct}%')
        
                   
        st.success(f'Predicted Status of Oil Viscosity on {p4}/{p3}/{p2} will be : {status} ')
        
        st.success(f'Predicted Result of Oil Viscosity on {p4}/{p3}/{p2} will be : {pred_value} ')

        
        st.info("""
                   - Warning Range : -10% to +10%
                   - Danger Range : -30% to +30%
                   
                   """)
        
        
    



 
if __name__ == '__main__':
    main()
