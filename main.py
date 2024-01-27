import streamlit as st
import pandas as pd
import numpy as np
import pylab
import matplotlib.pyplot as plt


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

df = pd.read_csv('./medication_usage_summary.csv')
bins = [0, 5, 10, 15, 20, float('inf')]
labels = ['1-5', '6-10', '11-15', '16-20', '20+']
df['category'] = pd.cut(df['user_count'], bins=bins, labels=labels, right=False)

category_counts = df['category'].value_counts(normalize=True) * 100


fig, ax = plt.subplots(figsize=(10, 6))
category_counts.plot(kind='bar', ax=ax)
ax.set_xlabel('Number of Users')
ax.set_ylabel('Percentage of Medications')
ax.set_title('Medication Usage by User Count Categories')
fig = fig.figure
st.pyplot(fig)
