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
    return email, name

def send_email(email, name):
    try:
        message = MIMEText(email, name)
        message['To'] = st.secrets['email_user']
        message['From'] = st.secrets['email_user']
        message['Subject'] = 'Giveaway Entry'

        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL('smtp.gmaail.com', context=context, port = 587)
        server.starttls()
        server.login(st.secrets['email_user'], st.secrets['email_pass'])
        server.send_message(st.secrets['email_user'], st.secrets['email_user'], message.as_string())
        server.quit()

        st.success('You have successfully been entered, please monitor your email to see if you won. \nDraws happen on the last Friday of evry month.')
    except:
        print('Unfortunately their was a submission error, please try again. If this error continues, please email "crisismild@gmail.com" with the subject "Please help me I am Drowning".') 




