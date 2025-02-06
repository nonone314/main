import streamlit as st
import pandas as pd

st.title("引継ぎくん")

option = st.selectbox(
    '料金所を選択してください',
    ['富山', '金沢', '福井','敦賀'],
    index = None,
    placeholder="料金所を選択してください")

keyword = option

with open('sample.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if keyword in line:
            st.writeline.strip())
