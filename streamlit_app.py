import streamlit as st
import mysql.connector

def connect_to_db_admin():
    return mysql.connector.connect(
        host="localhost",      
        user="root",  
        password="scma348", 
        database="education_001",
        port=3306
    )
def connect_to_db_student():
    return mysql.connector.connect(
        host="localhost",      
        user="student",  
        password="1234", 
        database="education_001"
    )
conn = connect_to_db_admin()
# Check if the connection was successful
if conn.is_connected():
    print("Connected to MySQL database")
cursor = conn.cursor()


st.title("EDUCATION-002")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
