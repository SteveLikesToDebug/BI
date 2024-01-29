import streamlit as st
import pandas as pd
import numpy as np

def intro():
    st.title("Welcome to the Healthcare Data Analysis App")
    st.write("This application provides insights into healthcare data from two perspectives: users and doctors.")
    st.write("Navigate through the app using the sidebar to explore different data visualizations and insights.")

def user_overview():
    st.title("User Overview")
    st.write("This section presents an overview of user data from the database.")
    # Add code to load and display user data, e.g.:
    # user_df = pd.read_csv('path_to_user_data.csv')
    # st.write(user_df)
    # st.bar_chart(user_df['some_column'])

def doctor_overview():
    st.title("Doctor Overview")
    st.write("This section is dedicated to data related to doctors.")
    # Add code to load and display doctor data, e.g.:
    # doctor_df = pd.read_csv('path_to_doctor_data.csv')
    # st.write(doctor_df)
    # st.line_chart(doctor_df['some_metric'])

def basnicka():
    st.title('Pro Leu')
    st.write("""
        Hello Leo,\\
        Dnes již tři týdny se známe,\\
        Bylo to velice krásné, příjemné a zrádné,\\
        Po tobě bude se mi teď stýskati,\\
        Doufám, že ve snech tvou krásu budu vídati,\\
        Nechť mají se tvé oči krásně,\\
        Těším se až uvidím tě jasně.
        """)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ('Introduction', 'User Overview', 'Doctor Overview','Básnička'))

if page == 'Introduction':
    intro()
elif page == 'User Overview':
    user_overview()
elif page == 'Doctor Overview':
    doctor_overview()
elif page == 'Básnička':
    basnicka()




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
st.write("""
    Tento graf znázorňuje, že pouhé jedno procento léků je běžně používáno velkou skupinou lidí 
    """)
#jsi lína píča, pracuj!!!

df3 = pd.read_csv('./medicament_count_graph.csv', sep=';')
df3 = df3[df3['count'] > 0]
category_counts3 = df3.set_index('category')['count']
fig3, ax3 = plt.subplots()
ax3.pie(category_counts3, labels=category_counts3.index, autopct='%1.1f%%', startangle=0)
ax3.axis('equal')
st.pyplot(fig3)
st.write("""
    Druhý koláčový graf říká, že 98% procent lidí má doma v průměru 20-25 léků, pouhá dvě procenta mají doma léků výrazně méně.
    """)
#mrdko