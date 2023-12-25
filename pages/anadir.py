import sqlite3
import pandas as pd
import streamlit as st

conn=sqlite3.connect("mydata.db")
c=conn.cursor()

def add_data(ID,population,generaciones,strain,type,position,gene):
    c.execute("INSERT INTO mutaciones(ID,population,generaciones,strain,type,position,gene) VALUES (?,?,?,?,?,?,?)",(ID,population,generaciones,strain,type,position,gene))
    conn.commit()

id=st.text_input("Ingresa ID: ")
population=st.text_input("Ingresa poblacion: ")
generaciones=st.text_input("Ingresa generacion: ")
strain=st.text_input("Ingresa cepa: ")
type=st.text_input("Ingresa tipo: ")
posicion=st.text_input("Ingresa posición: ")
gene=st.text_input("Ingresa gen: ")
if st.button("ADD"):
    add_data(id,population,generaciones,strain,type,posicion,gene)
    st.success("Datos ingresados")



