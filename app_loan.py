import streamlit as st
import pandas as pd
from PIL import Image
import pickle

from streamlit.proto.Balloons_pb2 import Balloons
model = pickle.load(open('C:/Users/lenovo/PycharmProjects/Loan_App/loanfinal.pkl', 'rb'))

def run():
    st.set_page_config(page_title='Loan Prediction using Machine Learning', page_icon=None, layout='wide', initial_sidebar_state='auto')
    
    st.title("Bank Loan Prediction using Machine Learning")
    img1 = Image.open('C:/Users/lenovo/PycharmProjects/Loan_App/pic1.jpg')
    img1 = img1.resize((700,250))
    st.image(img1,use_column_width=True)
    df= pd.read_csv('C:/Users/lenovo/PycharmProjects/Loan_App/train.csv')
    chart_1 = pd.DataFrame(df,columns=['LoanAmount'])
    chart_2 = pd.DataFrame(df,columns=['Dependents','Loan_Status'])
    

    st.subheader('Data Information : ')
    
    st.dataframe(df)
    st.write(df.describe())
    chart = st.area_chart(data=df, width=100, height=0, use_container_width=True)
    st.line_chart(df)
    st.area_chart(chart_1)
    fc=st.bar_chart(data =chart_2,height=200)
    
    st.sidebar.header('Predict Loan ')
    ## Account No
    account_no = st.sidebar.text_input('Account number')

    ## Full Name
    fn = st.sidebar.text_input('Full Name')

    ## For gender
    gen_display = ('Male','Female')
    gen_options = list(range(len(gen_display)))
    gen = st.sidebar.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.sidebar.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ## No of dependents
    dep_display = ('No','One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.sidebar.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])

    ## For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.sidebar.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For emp status
    emp_display = ('Unemployed','Self_Employed')
    emp_options = list(range(len(emp_display)))
    emp = st.sidebar.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    ## For Property status
    prop_display = ('Urban','Rural','Semi-Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.sidebar.selectbox("Property Area",prop_options, format_func=lambda x: prop_display[x])

    ## For Credit Score
    
    ## Applicant Monthly Income
    mon_income = st.sidebar.number_input("Applicant's Monthly Income($)",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.sidebar.number_input("Co-Applicant's Monthly Income($)",value=0)

    ## Loan AMount
    loan_amt = st.sidebar.number_input("Loan Amount",value=0)

    ## loan duration
    loan_amt_term = st.sidebar.slider("Loan Amount term in days($)",min_value=100,max_value=5000)

    cred_display = ('1.0','0.0')
    cred_options = list(range(len(cred_display)))
    cred = st.sidebar.radio("Credit Score",cred_options, format_func=lambda x: cred_display[x])


    if st.sidebar.button("Submit"):
        duration = 0
        if duration == 0:
            duration = 60
        if duration == 1:
            duration = 180
        if duration == 2:
            duration = 240
        if duration == 3:
            duration = 360
        if duration == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, loan_amt_term, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.spinner(text= 'Wait for it ')
            st.error(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'According to our Calculations, you are not eligible for the loan from our Bank'
            )
        else:
            st.spinner(text= 'Wait for it ')
            st.success(
                
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'Congratulations!! you are eligible for the loan from our Bank'
                
            )
            
            st.balloons()

run()