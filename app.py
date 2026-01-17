import streamlit as st

from views import overview, nationwide, statewise, insights

st.set_page_config(
    page_title="Aadhaar Enrolment Analytics",
    layout="wide"
)

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Overview", "Nationwide", "State-wise", "Insights"]
)

if page == "Overview":
    overview.page()

elif page == "Nationwide":
    nationwide.page()

elif page == "State-wise":
    statewise.page()

elif page == "Insights":
    insights.page()
