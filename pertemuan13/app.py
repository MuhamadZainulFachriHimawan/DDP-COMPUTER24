import streamlit as st

# st.streamlit("hello word")

dashboard = st.Page("./pages/dashboard.py", title="dashboard")
nabung = st.Page("./pages/nabung.py", title="nabung")

pg = st.navigation({
    "dasboard": [dashboard],
    "nabung": [nabung],
})
if "nabung" not in st.session_state:
    st.session_state['nabung'] = []
pg.run()