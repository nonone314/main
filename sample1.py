import streamlit as st
import pandas as pd

st.title("引継ぎくん")

option = st.selectbox(
    '料金所を選択してください',
    ['富山', '金沢', '福井','敦賀'],
    index = None,
    placeholder="料金所を選択してください")

keyword = option

if option == "富山":
	filtered_df = df[df['料金所'].str.contains(keyword)]
	st.write(filtered_df)

if option == "金沢":
	filtered_df = df[df['料金所'].str.contains(keyword)]
	st.write(filtered_df)

if option == "福井":
	filtered_df = df[df['料金所'].str.contains(keyword)]
	st.write(filtered_df)

if option == "敦賀":
	filtered_df = df[df['料金所'].str.contains(keyword)]
	st.write(filtered_df)