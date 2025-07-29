import streamlit as st
import requests

# Replace 'service1' with the name defined in render.yaml
SERVICE1_URL = "http://service1:9910"

st.title("Streamlit App Connecting to Service 1")

if st.button("Get Data from Service 1"):
    try:
        response = requests.get(f"{SERVICE1_URL}/your-endpoint")
        st.write("Response from Service 1:", response.json())
    except Exception as e:
        st.error(f"Error connecting to Service 1: {e}")