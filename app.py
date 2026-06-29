import streamlit as st

st.title("陸上100mタイム換算アプリ ")

distance = st.number_input("走った距離(m)を入力してください", value=200)
time = st.number_input("タイム(秒)を入力してください", value=22.0)

if st.button("換算する！"):
    converted_time = time * (100 / distance) ** 1.06
    st.success(f"あなたの100m換算タイムは: {converted_time:.2f} 秒です！")
