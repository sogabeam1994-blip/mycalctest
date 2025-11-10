import streamlit as st
import requests

st.title("🧮 Arithmetic Calculator")

# Input fields
a = st.number_input("Enter first number", value=0.0)
b = st.number_input("Enter second number", value=0.0)

# Operation dropdown
operation = st.selectbox("Choose operation", ["add", "subtract", "multiply", "divide"])

# Trigger calculation
if st.button("Calculate"):
    try:
        response = requests.post(
            "http://localhost:8000/calculate",
            json={"a": a, "b": b, "operation": operation}
        )
        data = response.json()
        if "result" in data:
            st.success(f"Result: {data['result']}")
        else:
            st.error(data.get("error", "Unknown error"))
    except Exception as e:
        st.error(f"Failed to connect to backend: {e}")
