# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:05:48 2022

@author: Yashdip
"""

#Imports

import seaborn as sns
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#1 Title

st.title('Data Analysis')
st.subheader('Data analysis using Python & Streamlit')

#2 Upload data

upload=st.file_uploader('Upload your dataset in CSV format')

if upload is not None:
    data=pd.read_csv(upload)


#3 Show dataset:
    
    if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head())
        elif st.button('Tail'):
            st.write(data.tail())
            
#4 Check datatype of each column
#if upload is not None:
#    if st.checkbox('Datatype of each column'):
 #       st.text('Datatypes')
  #      st.write(data.dtypes)
  
#5 Find shape of the data


if upload is not None:
    data_shape=st.radio('Dimensions of the dataset',('Rows','Columns'))
    if data_shape=='Rows':
        st.text('No. of rows')
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text('No. of columns')
        st.write(data.shape[1])
        
#6 Find null values in the dataset

if upload is not None:
    test=data.isnull().values.any()
    if test:
        if st.checkbox('Null values'):
            fig, ax = plt.subplots()
            sns.heatmap(data.isnull(), ax=ax)
            st.write(fig)
    else:
        st.success('Congrats!!! No missing values')
        
#6 Find duplicate values in the dataset:
    
if upload is not None:
    if data.duplicated ().any():
        #duplicate=data[data.duplicated().any()]
        st.warning('This dataset contains some duplicate values')
        dup_opt=st.selectbox('Do you wish to remove the duplicate values?', ('Yes','No'))
        if dup_opt=='Yes':
            data.drop_duplicates(inplace=True)
            st.text('Duplicate values removed')
        if dup_opt=='No':
            st.text('Duplicate values not removed')
            
#7 Get overall statistics

if upload is not None:
    if st.checkbox('Summary of the dataset'):
        st.write(data.describe())
        
#8 About

if st.button('About App'):
    st.text('Built with Streamlit')
    st.text('Developed by Yashdip Hande')