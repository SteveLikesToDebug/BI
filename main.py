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


df = pd.read_csv('./doctor_prescription_counts.csv', sep=';')
st.write(df)


import matplotlib.pyplot as plt
df2 = pd.read_csv('./medication_usage_summary.csv', sep=';')
bins = [0, 5, 10, 15, 20, float('inf')]
labels = ['1-5', '6-10', '11-15', '16-20', '20+']
df2['category'] = pd.cut(df2['No. users taking'], bins=bins, labels=labels, right=False)

category_counts = df2.groupby('category', observed=True)['Medication Name'].count()

fig, ax = plt.subplots(figsize=(10, 6))
category_counts.plot(kind='bar', ax=ax)
ax.set_xlabel('Number of Users')
ax.set_ylabel('Number of Medication Names')
ax.set_title('Number of Medication Names by User Count Categories')

#plt.show()
st.pyplot(fig)



fig, ax = plt.subplots()
ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')

st.pyplot(fig)
#jsi lína píča, pracuj!!!

df3 = pd.read_csv('./medicament_count_graph.csv', sep=';')
category_counts3 = df3.set_index('category')['count']
fig3, ax3 = plt.subplots()
ax3.pie(category_counts3, labels=category_counts3.index, autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
st.pyplot(fig3)
#mrdko