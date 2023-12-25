import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn=sqlite3.connect("mydata.db")
c=conn.cursor()
sql_query = pd.read_sql_query ('SELECT * FROM mutaciones', conn)
df = pd.DataFrame(sql_query, columns = ["ID","population","generaciones","strain","type","position","gene"])
conteo1=df['type'].value_counts()["SNP"]
conteo2=df['type'].value_counts()["DEL"]
conteo3=df['type'].value_counts()["INS"]
x=[conteo1,conteo2,conteo3]
labels = ['SNP', 'DEL', 'INS']
chart_data = pd.DataFrame(x,labels)
st.bar_chart(chart_data)
