import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

st.set_page_config(
    page_title="Badminton Rules Assistant",
    page_icon="🏸",
    layout="centered",
)

st.title("🏸 BWF Badminton Rules Assistant")
st.markdown("Ask me anything about badminton court dimensions, scoring systems, serving rules, faults, lets, and match regulations!")
