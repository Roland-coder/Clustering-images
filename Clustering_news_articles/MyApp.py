import streamlit as st
import pandas as pd


st.write("""
         
# Clustering News Articles
         
         """)

st.markdown('<h4>This web page shows articles from dailymail.co.uk grouped in 5 clusters according to content similarity</h4>', unsafe_allow_html=True)


st.markdown('<p>Bellow is the list of all articles collected grouped by <b>article title</b> and <b>article link</b></p>', unsafe_allow_html=True)

df_all_articles = pd.read_csv("dailymail_scrapped_articles_.csv", usecols=["Article Title", "Article Link"])

st.write(df_all_articles)


st.markdown('<p>Bellow is the list of all articles grouped in <b>Cluster 0</b></p>', unsafe_allow_html=True)

df_cluster_0 = pd.read_csv("clusters/cluster0.csv", usecols=["Article Title", "Article Link"])

st.write(df_cluster_0)


st.markdown('<p>Bellow is the list of all articles grouped in <b>Cluster 1</b></p>', unsafe_allow_html=True)

df_cluster_1 = pd.read_csv("clusters/cluster1.csv", usecols=["Article Title", "Article Link"])

st.write(df_cluster_1)


st.markdown('<p>Bellow is the list of all articles grouped in <b>Cluster 2</b></p>', unsafe_allow_html=True)

df_cluster_2 = pd.read_csv("clusters/cluster2.csv", usecols=["Article Title", "Article Link"])

st.write(df_cluster_2)


st.markdown('<p>Bellow is the list of all articles grouped in <b>Cluster 3</b></p>', unsafe_allow_html=True)

df_cluster_3 = pd.read_csv("clusters/cluster3.csv", usecols=["Article Title", "Article Link"])

st.write(df_cluster_3)


st.markdown('<p>Bellow is the list of all articles grouped in <b>Cluster 4</b></p>', unsafe_allow_html=True)

df_cluster_4 = pd.read_csv("clusters/cluster4.csv", usecols=["Article Title", "Article Link"])

st.write(df_cluster_4)



