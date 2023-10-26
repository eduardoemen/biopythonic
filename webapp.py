import sqlite3
import streamlit as st
import pandas as pd

conn=sqlite3.connect("ltee.db")
c=conn.cursor()



def add_data(pop,g,tipo,pos,mut,gen):
    c.execute("INSERT INTO populations(pop,g,tipo,pos,mut,gen) VALUES (?,?,?,?,?,?)",(pop,g,tipo,pos,mut,gen))
    conn.commit()

menu=["Inicio","Ver","Añadir","Buscar"]
choice=st.sidebar.selectbox("Menu",menu)

if choice=="Añadir":
    pop=st.text_input("Ingresa poblacion: ")
    g=st.text_input("Ingresa generacion: ")
    tipo=st.text_input("Ingresa tipo: ")
    pos=st.text_input("Ingresa posicion: ")
    mut=st.text_input("Ingresa mutacion: ")
    gen=st.text_input("Ingresa gen: ")
    if st.button("ADD"):
        add_data(pop,g,tipo,pos,mut,gen)
        st.success("Datos ingresados")

if choice=="Ver":
    sql_query = pd.read_sql_query ('SELECT * FROM populations', conn)
    df = pd.DataFrame(sql_query, columns = ['pop', 'g', 'tipo',"pos","mut","gen"])
    st.dataframe (df)
    

