import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    df = pd.read_csv(stringio)
    c=df['gene'].value_counts()
    
    data_as_csv= c.to_csv(index=False).encode("utf-8")
    st.download_button(
    "Download data as CSV", 
     data_as_csv, 
    "benchmark-tools.csv",
    "text/csv",
    key="download-tools-csv",
    )
    