import streamlit as st

st.title("Ini Halaman Nabung")

with st.form("nabung"):
    nama = st.text_input("masukan nama")
    nominal = st.number_input("masukan nominal nabung")
    submitButton = st.form_submit_button("simpan")

    if submitButton:
        st.write(nama)
        st.session_state['nabung'].append({
            "nama" : nama,
            "nominal": nominal,
        })
        st.success("berhasil menabung")
        