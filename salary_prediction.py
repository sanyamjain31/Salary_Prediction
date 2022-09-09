import streamlit as st
import pickle

model = pickle.load(open('./Model/Model2.pkl', 'rb'))

st.markdown("<h1 style='text-align:centre;color:Green;' ><b>SALARY PREDICTION BY USING ML </b></h>",
            unsafe_allow_html=True)

name = st.text_input("Enter The Candidate Name Here : ")
university = st.text_input("Enter The University Name : ")
cat = st.selectbox("Enter The University Category : ", ('Tier1', 'Tier2', 'Tier3'))
if cat == 'Tier1':
    cat = 1
elif cat == 'Tier2':
    cat = 2
elif cat == 'Tier3':
    cat = 3
backlogs = st.selectbox("Enter The Number Of Your Backlogs : ", (0, 1))
cgpa = st.text_input("Enter Your CGPA : ")
year_of_passout = st.selectbox("Enter Your Year Of Passout : ", (2020, 2021))
qualification = st.selectbox("Enter Your Highest Degree : ", ('M.Tech', 'B.Tech', 'B.SC', 'BE'))
if qualification == 'M.Tech':
    qualification = 1
elif qualification == 'B.Tech':
    qualification = 2
elif qualification == 'B.SC':
    qualification = 3
elif qualification == 'BE':
    qualification = 4

if st.button('SUBMIT'):
    st.markdown(name, "from", university)
    st.markdown("<h1 style= 'color:Green';' ><b>Expected Salary :</b></h>", unsafe_allow_html=True)
    output = round(model.predict([[cat, backlogs, cgpa, year_of_passout, qualification]])[0], 4)
    st.header(f"Hi {name} , Your Expected Salary In Rupees is {output} ")
