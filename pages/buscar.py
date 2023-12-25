import sqlite3
import pandas as pd
import streamlit as st

conn=sqlite3.connect("mydata.db")
c=conn.cursor()

sql_query = pd.read_sql_query ('SELECT * FROM mutaciones', conn)
df = pd.DataFrame(sql_query, columns = ["ID","population","generaciones","strain","type","position","gene"])



options = st.multiselect(
    'Elige tipo de mutación',
    ['SNP', 'INS', 'DEL', 'MOB'])
filtered_df = df[df["type"].isin(options)]
st.dataframe(filtered_df)


min_val, max_val = st.slider('Select range of values', min(df["ID"]), max(df["ID"]), (min(df["ID"]), max(df["ID"])))
filtered_df = df[(df["ID"] >= min_val) & (df["ID"] <= max_val)]
st.dataframe(filtered_df)


if st.checkbox('ARA-1'):
    rd = df[df['population']=="Ara-1"]
    st.dataframe(rd)
if st.checkbox('ARA-2'):
    rd = df[df['population']=="Ara-2"]
    st.dataframe(rd)
if st.checkbox('ARA-3'):
    rd = df[df['population']=="Ara-3"]
    st.dataframe(rd)


generation=[500,1000,2000]
elecc=st.selectbox("Selecciona Generación",generation)
if elecc==500:
        
        mask = df['generaciones'].isin(["500"])
        st.dataframe(df[mask])
if elecc==1000:
        
        mask = df['generaciones'].isin(["1000"])
        st.dataframe(df[mask])
if elecc==2000:
        
        mask = df['generaciones'].isin(["2000"])
        st.dataframe(df[mask])





















    