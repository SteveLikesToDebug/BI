import streamlit as st
import pandas as pd
import numpy as np



st.write("""
Hello Leo,\\
Dnes již tři týdny se známe,\\
Bylo to velice krásné, příjemné a zrádné,\\
Po tobě bude se mi teď stýskati,\\
Doufám, že ve snech tvou krásu budu vídati,\\
Nechť mají se tvé oči krásně,\\
Těším se až uvidím tě jasně.
""")


df = pd.read_csv('./doctor_prescription_counts.csv')
st.write(df)




