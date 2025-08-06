import streamlit as st
import pandas as pd 
import numpy as np

## Title of application
st.title("Hello Streamlit")

## Display some simple text
st.write("This is some simple text")

## Create a simple df
df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

## Display the Dataframe
st.write("Here is Df")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b', 'c'])
st.line_chart(chart_data)
st.line_chart(df)
