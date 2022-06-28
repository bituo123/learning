import streamlit as st
st.set_page_config(page_title="Plottin")
st.write(111)
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
