import streamlit as st
import pandas as pd


st.title("Image Cluster App")
st.header("Clustering Images Of E Commerce Products")
st.write("This web app shows clusters of different amazon products based on description of the different product images")


df = pd.read_csv('clustered_description.csv')
grouped = df.groupby('cluster')

for name, group in grouped:
  st.write("Below are the products and description in cluster ", name)
  st.write(group[['product_name','description']])
