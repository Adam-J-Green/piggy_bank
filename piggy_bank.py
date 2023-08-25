import streamlit as st
import pandas as pd
import piggy_bank_funcs as pb
from PIL import Image

def main():
    im = Image.open('piggy.png')
    col1, col2 = st.columns([1,1])

    with col1:
        st.image(im)

    with col2:
        pb.input_email()

    pb.send_email()


if __name__ == '__main__':
    main()



