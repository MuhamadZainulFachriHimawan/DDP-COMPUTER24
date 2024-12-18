import streamlit as st

st.title("Ini Dashboar:")
st.session_state['nabung']

jumlah = 0
for session in st.session_state['nabung']:
    jumlah += session['nominal']

st.write("total nominal menabung sebesar",jumlah)    

