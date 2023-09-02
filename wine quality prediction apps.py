# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 18:38:26 2023

@author: kiru
"""

import numpy as np
import pickle
import streamlit as st
# loading the saved model
loaded_model=pickle.load(open('C:/Users/kiru/Desktop/machine learing project/web pages/wine quality/wine_model.sav','rb'))

# creating a function for prediction
def wine_prediction(input_data):
    # changing the dataset to numpy array 
    input_data_asnumpy_array=np.asarray(input_data)
    # reshaped the input data to predict in each instance
    input_data_reshaped=input_data_asnumpy_array.reshape(1,-1)


    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==1):
        return 'Good Quality Wine'
    else:
        return 'Bad Quality Wine'
    

    
def main():
    # giving a title
    st.title('Wine Quality Prediction Web Apps')
    
    #getting the input data from user
    
    fixedacidity=st.text_input('level of fixed acidity')
    volatileacidity=st.text_input('Glucosevolatile acidity level')
    citricacid=st.text_input('citric acid value')
    residualsugar=st.text_input('residual sugar value')
    chlorides=st.text_input('chlorides level')
    freesulfurdioxide=st.text_input('free sulfur dioxide value')
    totalsulfurdioxide=st.text_input('total sulfur dioxide value')
    density=st.text_input('density value')
    pH=st.text_input('pH values')
    sulphates=st.text_input('sulphates values')
    alcohol=st.text_input('alcohols values')
  
    # code for prediction
    quality=''
    
    # creating a button for prediction
    
    if st.button('Quality Result'):
        quality=wine_prediction([fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol])
        
    st.success(quality)




if __name__ =='__main__':
    main()


    
   
