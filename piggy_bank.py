import streamlit as st
import piggy_bank_funcs as pb
from PIL import Image


def main():
    st.title('The Dank Piggy Bank')
    st.write('Thank you for your contributions to the family piggy bank. These dollars are going toward making the world a better place. \nAs a thank you, I welcome you to submit your email to be entered into a draw for a fun giveaway. \nDraws will happen on the last Friday of every month with the value of the prize reflecting the piggy bank contributions for the month.')
    im = Image.open('piggy.png')
    col1, col2 = st.columns([1,1])

    with col1:
        st.image(im)

    with col2:
        email, name, transaction_id = pb.input_email()
        if st.button('Submit Entry'):
            pb.send_email(email, name, transaction_id)



if __name__ == '__main__':
    main()



