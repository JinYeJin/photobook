import streamlit as st
# from datetime import date, datetime
import datetime

st.title("#my_storage")

uploadPhoto = st.file_uploader("Press to upload your memories 😆", accept_multiple_files=True, type="png")
default_date = datetime.date(1999, 1, 1)

if uploadPhoto:
    with st.form("my_form"):
        st.write("Please select your date")
        uploadDate = st.date_input("Date input", value=default_date)
        submitted = st.form_submit_button("Submit")

        if submitted:
            if uploadDate == default_date:
                st.write("Date not changed, Please select your date.")
            else:
                st.write("Date changed. Write your code below what you want.")
