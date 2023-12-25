
import sqlite3
import pandas as pd
import streamlit as st


conn = sqlite3.connect('mydata.db')
c = conn.cursor()


col1, col2= st.columns(2)

with col1:
    st.write("Eliminar")
    id=st.text_input("Ingresa ID de la fila a eliminar: ")    
    if st.button("Eliminar"):
        c.execute('DELETE from mutaciones WHERE ID=?', (id,) )
        conn.commit()
        st.write("Datos eliminados")  

with col2:
    st.write("Actualizar")
    id=st.text_input("Ingresa ID: ")    
    pobl=st.text_input("Ingresa nueva población: ")
    generacion=st.text_input("Ingresa nueva generación: ")
    if st.button("Actualizar"):
        c.execute('''UPDATE mutaciones SET population=?, generaciones=?  WHERE ID=?''', (pobl,generacion,id) )
        conn.commit()
        st.write("Datos actualizados")
    
