import streamlit as st
import smtplib
import email
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image


def input_email():
    st.write('Please Submit Your Email Address to be Entered to Win the Big Prize')
    email = st.text_input(label='Email Address')
    name = st.text_input(label='Please Enter Your Name')
    transaction_id = st.text_input(label = 'Please Enter Your Transaction ID')
    return email, name, transaction_id

def send_email(email, name, transaction_id):
    message = email+'/'+name+'/'+transaction_id
    try:
        message = MIMEText(message)
        message['To'] = st.secrets['email_user']
        message['From'] = st.secrets['email_user']
        message['Subject'] = 'Giveaway Entry'

        context = ssl.create_default_context()
        server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
        server.starttls(context=context)
        server.login(st.secrets['email_user'], st.secrets['email_pass'])
        server.send_message(message, st.secrets['email_user'], st.secrets['email_user'])
        st.success('You have successfully been entered, please monitor your email to see if you won. \n Please note, regardless of the number of times you submit your email, you will recieve only 1 entry per donation. Feel free to scan the QR again to make a second donation!')
    except Exception as error:
        print(error)
        print('Unfortunately their was a submission error, please try again. If this error continues, please email "crisismild@gmail.com" with the subject "Please help me I am Drowning".') 




