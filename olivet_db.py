import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import plotly.express as px
import plotly.graph_objects as go
import time
import openpyxl
import altair as alt

with st.sidebar:
    st.write("Welcome to The Methdodist Church Ghana")
    st.write("Dansoman circuit")
    
mode = st.sidebar.radio('Please choose your society',['Mt.Olivet', 'Grace', 'Ebenezer','Maranatha','Sukura'])

if mode == 'Grace':
    st.header('Page under construction')

elif mode == 'Ebenezer':
    st.header('Page under construction')

elif mode == 'Maranatha':
    st.header('Page under construction')

elif mode == 'Sukura':
    st.header('Page under construction')

elif mode == 'Mt.Olivet':
    st.header("Welcome to Mt.Olivet")
    st.write('Here you can preview our database')

    
    # function to return age groupls
    def generate_age_group(df):
        age_group = []
        for index, row in df.iterrows():
            if row.Age <=6:
                age_group.append('0-6')
            elif row.Age in range (7,10):
                age_group.append('7-9')
            elif row.Age in range (10,13):
                age_group.append("10-12")
            elif row.Age in range (13,16):
                age_group.append("13-15")
            elif row.Age == 123:
                age_group.append("date of birth not stated")
            else:
                age_group.append("above 15")
        return age_group

    # Function to read excel data
    @st.cache
    def names(df):            
        cols = ['Center','First Name','Middle Name','Last Name','Gender','Date of Birth',"Parent's Name", "Parent's Contact","Age"]
        int_cols = ["Parent's Contact","Age"]
        # Beginners
        beginners = pd.read_excel(df, sheet_name='beginners').filter(cols)
        beginners["age_group"] = generate_age_group(beginners)
    
        # class 1 and 2
        class_1_2Df = pd.read_excel(df, sheet_name='class_1_2').filter(cols)
        class_1_2Df["age_group"] = generate_age_group(class_1_2Df)
    
        # class 3
        class_3Df = pd.read_excel(df, sheet_name='class_3').filter(cols)
        class_3Df["age_group"] = generate_age_group(class_3Df)
    
        # class 4
        class_4Df = pd.read_excel(df, sheet_name='class_4').filter(cols)
        class_4Df["age_group"] = generate_age_group(class_4Df)
    
        # class 5
        class_5Df = pd.read_excel(df, sheet_name='class_5').filter(cols)
        class_5Df["age_group"] = generate_age_group(class_5Df)
    
        # class 6
        class_6Df = pd.read_excel(df, sheet_name='class_6').filter(cols)
        class_6Df["age_group"] = generate_age_group(class_6Df)
    
        # jhs 1
        jhs_1Df = pd.read_excel(df, sheet_name='jhs_1').filter(cols)
        jhs_1Df["age_group"] = generate_age_group(jhs_1Df)
    
        # timothy
        timothyDf = pd.read_excel(df, sheet_name='timothy').filter(cols)
        timothyDf["age_group"] = generate_age_group(timothyDf)
    
        # sahara
        saharaDf = pd.read_excel(df, sheet_name='sahara').filter(cols)
        saharaDf["age_group"] = generate_age_group(saharaDf)
    
        # ham
        hamDf = pd.read_excel(df, sheet_name='ham').filter(cols)
        hamDf["age_group"] = generate_age_group(hamDf)
    
        # wesley grammar
        wesgDf = pd.read_excel(df, sheet_name='wesley_grammar').filter(cols)
        wesgDf["age_group"] = generate_age_group(wesgDf)
    
        finalDf =  pd.concat([beginners, class_1_2Df, class_3Df, class_4Df, class_5Df, class_6Df, jhs_1Df, 
                         timothyDf, saharaDf, hamDf, wesgDf]
                         , axis=0)
        # col transformation
        #     convert = lambda x: int(x) if pd.notnull(x) else x
#     finalDf[int_cols] = finalDf[int_cols].astype({"Parent's Contact": 'int',"Age": 'int'})
    
        return finalDf
        
    excelDf = "olivet_db.xlsx"
    olivetDf = names(excelDf)
    head = olivetDf.head(20)
 
    if st.button('submit'):
        with st.spinner('Loading data'):
            time.sleep(1)
        st.write(head)

# count
    def count_plot(data): # works
        fig = px.histogram(data, x='Gender', color='Gender')
        fig.update_layout(
                title='Gender Count',
                xaxis_title='Gender',
                yaxis_title='Count'
                )
        st.plotly_chart(fig, use_container_width=True)

    # side by side
    def side_chart(df):
        chart = px.histogram(df,x='Center', color='Gender', barmode='group')
        chart.update_layout(
                title='Gender Count',
                xaxis_title='Center',
                yaxis_title='Count'
                )
        st.plotly_chart(chart, use_container_width=True)

    st.write("Pick a center to reveal gender statitics")
    box = st.selectbox('Choose a center',[None,'All Centers','Olivet','Wesley Grammar','Sahara','Ham','Control' ])

    if box == 'Olivet':
        oliveDf = olivetDf[olivetDf.Center == 'Mt.Olivet']
        count_plot(oliveDf)
    elif box == 'Wesley Grammar':
        wesg = olivetDf[olivetDf.Center == 'Wesley Grammar']
        count_plot(wesg)
    elif box == 'Sahara':
        sahara = olivetDf[olivetDf.Center == 'Sahara']
        count_plot(sahara)
    elif box == 'Ham':
        ham = olivetDf[olivetDf.Center == 'Ham']
        count_plot(ham)
    elif box == 'All Centers':
        st.write("Total number of Males and Females")
        count_plot(olivetDf)
        st.write('')
        st.write('Bar Chart comparing Centers')
        side_chart(olivetDf)

# Second Part showing age demography

    def age_count_plot(data): # works
        fig = px.histogram(data, x='age_group', color='age_group')
        fig.update_layout(
                title='Age Groupings',
                xaxis_title='Ages',
                yaxis_title='Count'
                )
        st.plotly_chart(fig, use_container_width=True)

   
    st.subheader("Age Statistics")

    if st.button('Check'):
        with st.spinner('Loading data'):
            time.sleep(1)
        st.write("Age bar plot")
        ageCountDf = age_count_plot(olivetDf) 

        